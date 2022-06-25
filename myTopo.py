from mininet.topo import Topo

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

		# Add switches
		switches = [self.addSwitch( 's1' ), self.addSwitch( 's2' ), self.addSwitch( 's3' ), self.addSwitch( 's4' )]

		# Add links
		self.addLink( upperLeftHost, switches[0] )
		self.addLink( bottomLeftHost, switches[0] )
		self.addLink( switches[0], switches[1] )
		self.addLink( switches[1], switches[2] )
		self.addLink( switches[2], switches[3] )
		self.addLink( switches[3], upperRightHost )
		self.addLink( switches[3], bottomRightHost )


topos = { 'linear': LinearTopology }


