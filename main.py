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


'''while True: 
        
    for a in range(20):
        pixels[a]=(255, 0, 0)
    pixels.show()
    time.sleep(2)
    for a in range(20):
        pixels[a]=(0, 0, 0)
    pixels.show()
    time.sleep(2)'''

'''def setAll(r, g, b):
   for a in range(20):
       pixels[a]=(r, g, b)
   pixels.show()

while True:
    print('starting main loop again')
    for t in range(256):
        setAll(0, t, 0)
        time.sleep(0.1)
    for t in range(255, -1, -1):
        setAll(0, t, 0)'''


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


'''for rainbow in range(20):
    pixels[rainbow]=colorwheel(255/20*rainbow)
    pixels.show()'''

movingRainbow = 0
'''while True:
    for r in range(20):
        pixels[r]=colorwheel((255/20*(r+movingRainbow))%255)  
        #pixels[r]=colorwheel((r+movingRainbow)/20)
        pixels.show()
    movingRainbow = movingRainbow+1'''

'''pixels[0]=(255, 0, 0)
pixels.show()'''

'''for a in range(20):
    pixels[a]=(255, 0, 0)
    pixels.show()'''

'''for a in range(20):
    pixels[a]=(255, 0, 0)
pixels.show()
bChange=0
while True:
    pixels.brightness = bChange / 20
    bChange=bChange+1
    pixels.show()
    time.sleep(.1)'''

'''while True:
    for red in range(20):
        pixels[red]=(255, 0, 0)
    pixels.show()
    for up in range(40):
        pixels.brightness=up/40
        pixels.show()
        time.sleep(.1)
    for down in range(40, 1, -1):
        pixels.brightness=down/40
        pixels.show()
        time.sleep(0.1)'''

'''while True:
    for cone in range(20):
        pixels[cone]=(255, 165, 0)
    pixels.show()
    time.sleep(0.3)
    for cone in range(20):
        pixels[cone]=(0, 0, 0)
    pixels.show()
    time.sleep(0.2)'''

'''while True:
    for cube in range(20):
        pixels[cube]=(145, 0, 255)
    pixels.show()
    time.sleep(0.3)
    for cube in range(20):
        pixels[cube]=(0, 0, 0)
    pixels.show()
    time.sleep(0.3)'''

count=0
while True:
    count=count+0.2

    '''for lowBattery in range(20):
        pixels[lowBattery]=(0, 255, 0)
    pixels.show()
    time.sleep(5/count)
    for lowBattery in range(20):
        pixels[lowBattery]=(240, 70, 0)
    pixels.show()
    time.sleep(1)'''

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
        pixels[lowBattery]=(255, 0, 0)

    

    '''else:
        for lowBattery in range(20):
            pixels[lowBattery]=(240, 70, 0)
        pixels.show()
        time.sleep(5/count)
        for lowBattery in range(20):
            pixels[lowBattery]=(255, 0, 0)
        pixels.show()
        time.sleep(1)'''

