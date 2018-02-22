from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import RPi.GPIO as GPIO

from time import sleep



def loop():
	mcp.output(3,1)     # turn on LCD backlight
	lcd.begin(16,2)     # set number of LCD lines and columns
	i = 0
	a = 0
	while(True):         
        #lcd.clear()
		if(a == 1):
			lcd.clear()
			lcd.setCursor(0,0)  # set cursor position
			lcd.message( 'Person erkannt!\n' )
			lcd.message( '----------------' )
			i = 0
		else:
			lcd.clear()
			lcd.setCursor(0,0)  # set cursor position
			lcd.message( 'Niemand erkannt!\n' )
			lcd.message( '----------------' )
			i = 0
		if (i = 100000)	
			if (GPIO.input(sensorPin)==GPIO.HIGH):
				a = 1
				i = 0
				print 'a = 1 wurde gesetzt'
			else: 
				a = 0
				i = 0
		i += 1

		
		
		
		
		
		
		
		
		
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
	mcp = PCF8574_GPIO(PCF8574_address)
except:
	try:
		mcp = PCF8574_GPIO(PCF8574A_address)
	except:
		print 'I2C Address Error !'
		exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    print 'Program is starting ... '
    sensorPin = 11
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(sensorPin, GPIO.IN)    # Set sensorPin's mode is input
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

