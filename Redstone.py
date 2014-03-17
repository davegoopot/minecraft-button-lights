import connect
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
#55 == Redstone Dust
Redstonedust = 55
Redstonerepeter = 93
Redstonelamp = 123
Lever = 69
				
world = connect.connect()
block_location = (-4, 0.0, 8.0)
block_type = block.Block(Redstonedust)
world.setBlock(block_location, block_type)

block_location = (-4, 0.0, 7.0)
block_type = block.Block(Redstonerepeter)
world.setBlock(block_location, block_type)	

block_location = (-4, 0.0, 6.0)
block_type = block.Block(Redstonelamp)
world.setBlock(block_location, block_type)	

block_location = (-4, 0.0, 9.0)
block_type = block.Block(Lever)
world.setBlock(block_location, block_type.id ,5)	