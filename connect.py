import mcpi.minecraft as minecraft

def connect():
	return minecraft.Minecraft.create("192.168.137.1", 4711)
