from mininet.topo import Topo

class MyTopo( Topo ):
	"Simple topology example."
	def __init__( self ):
		"Create custom topo."
		# Initialize topology
		Topo.__init__( self )
		
		# Add hosts 
		upperLeftHost = self.addHost( 'h1' )
		upperRightHost = self.addHost( 'h2' )
		bottomLeftHost = self.addHost( 'h3' )
		bottomRightHost = self.addHost( 'h4' )
		
		# Add switches
		leftSwitch = self.addSwitch( 's1' )
		rightSwitch = self.addSwitch( 's2' )

		# Add links
		self.addLink( upperLeftHost, leftSwitch )
		self.addLink( bottomLeftHost, leftSwitch )
		self.addLink( leftSwitch, rightSwitch )
		self.addLink( rightSwitch, upperRightHost )
		self.addLink( rightSwitch, bottomRightHost )

topos = { 'mytopo': ( lambda: MyTopo() ) }

