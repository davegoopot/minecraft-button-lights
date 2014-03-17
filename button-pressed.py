import connect
import mcpi.minecraft as minecraft
import mcpi.block as block
import RPi.GPIO as GPIO
import time

PIN=18

def gpio_setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def gpio_button_status():
	if GPIO.input(PIN):
		return "off"
	else:
		return "on"
	

def wait_for_button(world, location, block_type, button_state_fn):
	while True:
		state = button_state_fn()
		#print state
		block_set_type = block_type if (state == "on") else block.AIR
		world.setBlock(block_location, block_set_type)
		time.sleep(0.1)
			

if __name__ == "__main__":
	gpio_setup()
	world = connect.connect()
	block_location = (-4, 0.0, 3.0)
	block_type = block.BRICK_BLOCK
	wait_for_button(world, block_location, block_type, gpio_button_status)
