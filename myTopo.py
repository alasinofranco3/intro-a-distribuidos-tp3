from mininet.topo import Topo
import sys

class LinearTopology(Topo):
	"Simple topology example."
	def __init__(self, number_of_switches):
		"Create custom topo."
		# Initialize topology
		Topo.__init__( self )
		print("Creating topo with {} switches".format(str(number_of_switches)))
	
		# Add hosts 
		upperLeftHost = self.addHost( 'h1' )
		upperRightHost = self.addHost( 'h2' )
		bottomLeftHost = self.addHost( 'h3' )
		bottomRightHost = self.addHost( 'h4' )

        #Add switches
		switches = []
		for i in range(int(number_of_switches)):
			alias = "s"+str(i)
			switches.append(self.addSwitch(alias))

 		# Add links
		self.addLink( upperLeftHost, switches[0] )
		self.addLink( bottomLeftHost, switches[0] )

		for i in range(1,int(number_of_switches)):
			self.addLink( switches[i-1],switches[i])

		self.addLink( switches[int(number_of_switches)-1], upperRightHost )
		self.addLink( switches[int(number_of_switches)-1], bottomRightHost )


topos = { 'linear': LinearTopology }
