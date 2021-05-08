# Add your Python code here. E.g.
from microbit import *
import neopixel
import random
import music

Key_C = 0x0004
Key_CD = 0x0008
Key_D = 0x0010
Key_DE = 0x0020
Key_E = 0x0040
Key_F = 0x0080
Key_FG = 0x0100
Key_G = 0x0200
Key_GA = 0x0400
Key_A = 0x0800
Key_AB = 0x1000
Key_B = 0x2000 
Key_L = 0x0002
Key_M = 0x0001
Key_H = 0x4000

np = neopixel.NeoPixel(pin1, 3)
np.clear()

i2c.init()

def touch_key():
    i2c.write(0x50, bytes([8]))
    arr = i2c.read(0x50,2)
    val = arr[0] + arr[1]*256
    return val

def play_piano():
    while True:
        key_pressed = touch_key()
        if key_pressed == Key_C:
            music.play("C4:4")
        elif key_pressed == Key_CD:
            music.play("C#4:4")
        elif key_pressed == Key_D:
            music.play("D4:4")
        elif key_pressed == Key_DE:
            music.play("D#4:4")
        elif key_pressed == Key_E:
            music.play("E4:4")
        elif key_pressed == Key_F:
            music.play("F4:4")
        elif key_pressed == Key_FG:
            music.play("F#4:4")
        elif key_pressed == Key_G:
            music.play("G4:4")
        elif key_pressed == Key_GA:
            music.play("G#4:4")
        elif key_pressed == Key_A:
            music.play("A4:4")
        elif key_pressed == Key_AB:
            music.play("A#4:4")
        elif key_pressed == Key_B:
            music.play("B4:4")
        elif key_pressed == Key_L:
            np[0] = (5,0,0)
            np.show()
        elif key_pressed == Key_M:
            np[1] = (0,5,0)
            np.show()
        elif key_pressed == Key_H:
            np[2] = (0,0,5)
            np.show()
        
        sleep(200)

play_piano()





