from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import RPi.GPIO as GPIO
import Keypad 

from time import sleep

ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys =  [   '1','2','3','A',    #key code
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [12,16,18,22]        #connect to the row pinouts of the keypad
colsPins = [19,15,13,11]        #connect to the column pinouts of the keypad

def loop():
	keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
	keypad.setDebounceTime(50)      #set the debounce time
	mcp.output(3,1)     # turn on LCD backlight
	lcd.begin(16,2)     # set number of LCD lines and columns
	i = 0
	while(True):         
        #lcd.clear()
		if(i == 1000000):
			lcd.setCursor(0,0)  # set cursor position
			lcd.message( 'Hallo\n' )# display CPU temperature
			lcd.message( 'My name is Pi!' )   # display the time
		if(i == 1500000):
			lcd.setCursor(0,0)  # set cursor position
			lcd.message( 'How can i help you?' )# display CPU temperature
			lcd.message( '[9] Options' )# display the time
		if(i == 2000000):
			lcd.setCursor(0,0)  # set cursor position
			lcd.message( 'How can i help you?' )# display CPU temperature
			lcd.message( '[9] Options' )# display the time
		key = keypad.getKey()
		if(key != keypad.NULL):     #if there is key pressed, print its key code.
			lcd.clear()
			lcd.setCursor(0,0)
			lcd.message('Taste ' + key + ' pressed!')
		i = i + 1
		
		
		
		
		
		
		
		
		
        
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
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

