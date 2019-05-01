#! /usr/bin/python

#Imports
import RPi.GPIO as GPIO
import requests
from dynaconf import settings

wbHks = settings.WEBHOOKS

def button_callback(channel):
    print("Channel %s was pressed"%(channel))
    action = actionLookup[channel]
    if action == 'shutdown':
        print('Starting shut down sequence...')
        GPIO.cleanup()
        exit()
    elif action == 'toggleled':
        print('Toggle Led2')
        led2CS = GPIO.input(ledPins[1])
        if(led2CS == GPIO.HIGH):
            GPIO.output(ledPins[1],GPIO.LOW)
        else:
            GPIO.output(ledPins[1], GPIO.HIGH)
    else:
        requestURL = wbHks.TRIGGERURL.replace(wbHks.EVENTMERGETOK, action).replace(wbHks.KEYMERGETOK,settings.WEB_HOOKS_KEY)
        r = requests.post(requestURL,params={"value1":"none","value2":"none","value3":"none"})


#Set the GPIO warnings
GPIO.setmode(GPIO.BOARD)

#Turn off GPIO warnings
GPIO.setwarnings(False)

#Set a variable to hold the pin identity
button = settings.BUTTONS
ledPins = settings.LEDPINS
actionLookup = {}

#Set GPIO pin as input
for button in buttons:
    actionlookup[button.PIN] = button.EVENTNAME
    GPIO.setup(button.PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN, bouncetime=200)
    GPIO.add_event_detect(button.PIN,GPIO.RISING,callback=button_callback)

for pin in ledPins
    GPIO.setup(pin, GPIO.OUT)
    

print('Ready to listen')
GPIO.output(ledPin[0],GPIO.HIGH)

message = input('Press enter to quit\n\n')  

GPIO.cleanup()

