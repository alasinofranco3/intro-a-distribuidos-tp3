# -intro-a-distribuidos-tp3
tp3 - SDN - intro a distribuidos - FIUBA 


# Correr POX
./pox.py --verbose controller

# Correr Minet
sudo mn --custom myTopo.py --topo linear,4 --mac --arp --switch ovsk --controller remote

# H1 como server
h1 iperf -s -p 81 &

# H2 como client
h2 iperf -c h1 -p 81
