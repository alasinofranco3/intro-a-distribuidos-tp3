# Coursera :
# - Software Defined Networking ( SDN ) course
# -- Programming Assignment : Layer -2 Firewall Application Professor : Nick Feamster
# Teaching Assistant : Arpit Gupta
from pox.core import core
from config import FIREWALL_SWITCH, IP_HOST_1, RULE_3_HOST_1, RULE_3_HOST_2
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
from collections import namedtuple
import os
from pox.forwarding import l2_learning
import pox.lib.packet as pkt


# Add your imports here ...
log = core.getLogger()


# Add your global variables here ...
class Controller(EventMixin):
    def __init__(self) :
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module in switch {}".format(FIREWALL_SWITCH))
        self.firewall_switch = FIREWALL_SWITCH

    
    def _handle_ConnectionUp(self, event):
        # Add your logic here ...
        log.debug("Handling Connection Up for switch {}".format(event.dpid))
        #log.debug(event)
        
        if event.dpid == self.firewall_switch:
            self.build_firewall_rules(event)


    def build_firewall_rules(self, event):
        log.debug("Start building firewall rules for switch {}".format(event.dpid))

        self.build_port_80_rule(event)        
        self.build_host_1_port_5001_udp_rule(event)
        self.build_disable_host_communication_rule(event)

        log.debug("Finish building firewall rules")


    def build_port_80_rule(self, event):
        log.debug("Building port 80 rule")

        # Build match for TCP
        match = of.ofp_match(
            dl_type=pkt.ethernet.IP_TYPE,
            nw_proto=pkt.ipv4.TCP_PROTOCOL,
            tp_dst=80
        )

        self.drop_packet_with_match_and_send_msg_to_firewall(match, event)

        # Build match for UDP
        match = of.ofp_match(
            dl_type=pkt.ethernet.IP_TYPE,
            nw_proto=pkt.ipv4.UDP_PROTOCOL,
            tp_dst=80
        )

        self.drop_packet_with_match_and_send_msg_to_firewall(match, event)  

    
    def build_host_1_port_5001_udp_rule(self, event):
        log.debug("Building host 1, port 5001, protocolo UDP rule")

        # Build match for rule
        match = of.ofp_match(
            dl_type=pkt.ethernet.IP_TYPE,
            nw_proto=pkt.ipv4.UDP_PROTOCOL,
            tp_dst=5001,
            nw_src = IPAddr(IP_HOST_1)
        )

        self.drop_packet_with_match_and_send_msg_to_firewall(match, event)


    def build_disable_host_communication_rule(self, event):
        log.debug("Building disable host communication between host 1 and host 4 rule")

        match = of.ofp_match(
            dl_type=pkt.ethernet.IP_TYPE,
            nw_src = IPAddr(RULE_3_HOST_1),
            nw_dst = IPAddr(RULE_3_HOST_2),
        )

        self.drop_packet_with_match_and_send_msg_to_firewall(match, event)

        match = of.ofp_match(
            dl_type=pkt.ethernet.IP_TYPE,
            nw_src = IPAddr(RULE_3_HOST_2),
            nw_dst = IPAddr(RULE_3_HOST_1),
        )

        self.drop_packet_with_match_and_send_msg_to_firewall(match, event)


    def drop_packet_with_match_and_send_msg_to_firewall(self, match, event):
        msg = of.ofp_flow_mod()
        msg.match = match
        msg.actions.append(of.ofp_action_tp_port.set_dst(of.OFPP_NONE))
        event.connection.send(msg)


def launch():
    # Starting the Firewall module
    core.registerNew(Controller)
    l2_learning.launch()
