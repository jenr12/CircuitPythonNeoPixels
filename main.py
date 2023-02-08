# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.D5
num_pixels = 20

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)



print('Starting!')


###### knight Rider ######
'''while True:
    for forwards in range(20):
        pixels[forwards]=(255, 0, 0)
        pixels[forwards-1]=(75, 0, 0)
        pixels[forwards-2]=(0, 0, 0)
        #pixels[forwards+1]=(75, 0, 0)
        #pixels[forwards+2]=(0, 0, 0)
        if forwards == 18:
            pixels[forwards]=(255, 0, 0)
        if forwards == 19:
            pixels[forwards]=(75, 0, 0)
        pixels.show()
        time.sleep(1)
    for backwards in range(19, 0, -1):
        pixels[backwards]=(0, 0, 0)
        pixels[backwards-1]=(255, 0, 0)
        pixels.show()
        time.sleep(0.09)'''

##### Rainbow Circle ######
'''for rainbow in range(20):
    pixels[rainbow]=colorwheel(255/20*rainbow)
    pixels.show()

movingRainbow = 0
while True:
    for r in range(20):
        pixels[r]=colorwheel((255/20*(r+movingRainbow))%255)  
        #pixels[r]=colorwheel((r+movingRainbow)/20)
        pixels.show()
    movingRainbow = movingRainbow+1'''


##### FUNCTIONS FOR ROBOT #######

#allianceColor=(255, 0, 0)
allianceColor=(0, 0, 255)

def blinkingCube():
    for cube in range(15, 20, 1):
        pixels[cube]=(255, 0, 0)
    for cube in range(0, 15):
        pixels[cube]=(145, 0, 255)
    pixels.show()
    time.sleep(0.3)
    for cube in range(15):
        pixels[cube]=(0, 0, 0)
    pixels.show()
    time.sleep(0.2)
    
while True:
    blinkingCube()



def blinkingCone():
    for cube in range(15, 20, 1):
        pixels[cube]=(255, 0, 0)
    for cone in range(0, 15):
        pixels[cone]=(255, 165, 0)
    pixels.show()
    time.sleep(0.3)
    for cone in range(15):
        pixels[cone]=(0, 0, 0)
    pixels.show()
    time.sleep(0.2)

#while True:
    #blinkingCone()


def enable():
    def setAll(r, g, b):
        for a in range(20):
            pixels[a]=(r, g, b)
        pixels.show()

        for enable in range(20):
            pixels[enable]=(255, 0, 0)

        for t in range(256):
            setAll(0, t, 0)
        for t in range(255, -1, -1):
            setAll(0, t, 0)
#while True:
    #enable()


count=0 
def enabled():
    #while True:

        print('start of loop 1')
        for alliance in range(15, 20, 1):
            pixels[alliance]=(255, 0, 0)

        steps=30
        wait=0.04
        for countdown in range(steps, 1, -1):
            for enabled in range(0, 15):
                pixels[enabled]=(0, 255*countdown/steps, 0)
            pixels.show()
            time.sleep(wait)
            print('brightness down')

        for countup in range(1, steps, 1):
            print('in loop 1')
            for enabled in range(0, 15):
                pixels[enabled]=(0, 255*countup/steps, 0)
            pixels.show()
            time.sleep(wait)
            print('brightness up')

#while True:
 #   enabled()


def noCode():
    #while True:
    for noCode in range(20):
        pixels[noCode]=(255, 0, 0)
    pixels.show()
    time.sleep(0.3)
    for noCode in range(20):
        pixels[noCode]=(0, 0, 0)
    pixels.show()
    time.sleep(0.3)
#while True:
    #noCode()

def disabled():
    for disabled in range(0, 15):
        pixels[disabled]=(255, 0, 0)
        pixels.show()
    for alliance in range(15, 20):
        pixels[alliance]=(allianceColor)
        pixels.show
#while True:
    #disabled()




while True:
    print('start loop')

    print('starting blinkingCube')
    blinkingCube()
    time.sleep(1)
    print('ending blinkingCube')

    print('starting blinkingCone')
    blinkingCone()
    time.sleep(1)
    print('ending blinkingCone')

    print('starting enabled')
    enabled()
    time.sleep(1)
    print('ending enabled')

    print('starting noCode')
    noCode()
    time.sleep(1)
    print('ending noCode')

    print('starting disabled')
    disabled()
    time.sleep()
    print('ending disabled')



####### EXTRAS ########

'''def lowBattery():
    for lowBattery in range(20):
        pixels[lowBattery]=(0, 255, 0)
    pixels.show()
    time.sleep(5/count)
    for lowBattery in range(20):
        pixels[lowBattery]=(240, 70, 0)
    pixels.show()
    time.sleep(1)

    if count < 4:
        for lowBattery in range(20):
            pixels[lowBattery]=(0, 255, 0)
        pixels.show()
        time.sleep(5/count)
        for lowBattery in range(20):
            pixels[lowBattery]=(240, 70, 0)
        pixels.show()
        time.sleep(1)

    elif count >= 4 and count >= 8:
        for lowBattery in range(20):
            pixels[lowBattery]=(240, 70, 0)
        pixels.show()
        time.sleep(5/(count-3))
        for lowBattery in range(20):
            pixels[lowBattery]=(255, 0, 0)
        pixels.show()
        time.sleep(1)

    else:
        pixels[lowBattery]=(255, 0, 0)'''
