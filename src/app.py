#! /usr/bin/python

#Imports
import RPi.GPIO as GPIO
import requests
from dynaconf import settings

wbHks = settings.WEBHOOKS

def button_callback(channel):
    print("Channel %s was pressed"%(channel))
    if channel == 16:
        print('Starting shut down sequence...')
        GPIO.cleanup()
        exit()
    elif channel == 18:
        print('Toggle Led2')
        led2CS = GPIO.input(ledPin2)
        if(led2CS == GPIO.HIGH):
            GPIO.output(ledPin2,GPIO.LOW)
        else:
            GPIO.output(ledPin2, GPIO.HIGH)
    else:
        requestURL = wbHks.TRIGGERURL.replace(wbHks.EVENTMERGETOK, settings.BUTTON1EVENTNAME).replace(wbHks.KEYMERGETOK,settings.WEB_HOOKS_KEY)
        r = requests.post(requestURL,params={"value1":"none","value2":"none","value3":"none"})


#Set the GPIO warnings
GPIO.setmode(GPIO.BOARD)

#Turn off GPIO warnings
GPIO.setwarnings(False)

#Set a variable to hold the pin identity
pinId1 = 11
pinId2 = 13
pinId3 = 15
pinId4 = 16
pinId5 = 18

ledPin1 = 22
ledPin2 = 24

#Set GPIO pin as input
GPIO.setup(pinId1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pinId1,GPIO.RISING,callback=button_callback)

GPIO.setup(pinId2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pinId2,GPIO.RISING,callback=button_callback)

GPIO.setup(pinId3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pinId3,GPIO.RISING,callback=button_callback)

GPIO.setup(pinId4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pinId4,GPIO.RISING,callback=button_callback)

GPIO.setup(pinId5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pinId5,GPIO.RISING,callback=button_callback)

GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)

print('Ready to listen')
GPIO.output(ledPin1,GPIO.HIGH)

message = input('Press enter to quit\n\n')  

GPIO.cleanup()

