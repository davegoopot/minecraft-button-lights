import connect
import mcpi.minecraft as minecraft
import mcpi.block as block
import RPi.GPIO as GPIO
from time import sleep

PIN=12

def gpio_setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIN, GPIO.OUT)
	GPIO.output(PIN, GPIO.LOW)


def print_changed_block(new_block_type):
	print("Changed.  New block = " + str(new_block_type))
	if new_block_type == block.AIR:
		GPIO.output(PIN, GPIO.LOW)
	else:
		GPIO.output(PIN, GPIO.HIGH)
	
def monitor_block(world, block_location, on_change_fn):
	[x,y,z] = block_location

	old_block_state = 0
	while True:
		new_block_state = world.getBlock(x, y, z)
		if new_block_state != old_block_state:
			on_change_fn(new_block_state)
			old_block_state = new_block_state
		sleep(0.1)
	

if __name__ == "__main__":
	gpio_setup()
	world = connect.connect()
	block_location = (3, 0.0, 0.4)
	monitor_block(world, block_location, print_changed_block)


