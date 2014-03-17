import mcpi.minecraft as minecraft
import connect

world = connect.connect()
print("connected to world")

print world.player.getPos()
