import ssd1306
import machine
import utime as  time
import framebuf
import base64
import math
from GraphicDisplay import *
print("GurgleApps.com Pico Pong")
# would have used pin 1 & 2 but they were broken on one of our Pico Boards
speaker_pin = 16
play_button_pin = 2
left = 26
right = 27
clockPin = 1
dataPin = 0
bus = 0
mode_init = 1
mode_playing = 2
mode_game_over = 3
mode = mode_init # mode_init,mode_playing,mode_game_over
analog_pin_left = machine.ADC(left)
analog_pin_right = machine.ADC(right)
play_button = machine.Pin(play_button_pin,machine.Pin.IN, machine.Pin.PULL_DOWN)
speaker = machine.PWM(machine.Pin(speaker_pin))
speaker.duty_u16(0)
i2c = machine.I2C(bus,sda=machine.Pin(dataPin),scl=machine.Pin(clockPin))
display = OLED()
logoSmallB = b'aBn/gP//wH//4D//8B/w/AAf/gAP/wAH/4AD8MAAAeAAAPAAAHgAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAA4AAAAAAAOAAAAAACAOAAAAAAADgAAAAAAgCxAAAAAAHQAB4AMeIAscAAGMAB2AAeBPHiAJHsACmqAbwAGySBIhixLxwhr8H4ABEkgSIt8S+UIS3h+AARJIEiLfktsGE5IVIAFCSBoj2ZrbgoqSGYABckgeIhGe2MOOkgngATPIAiKQFthYBpIZgAEzwBIjgBD70ACSCYAB4AAaAQAQ0YAAEgmAAOAADgAAEMAAAAJpgAAAAAQAAADAAAAACADAAAHgAADwQAB4AAAw+AAP/AAH/gAD/wAB8P+A///Af//gP//wH/D////////////////w'
logoLargeB = b'gB//8A////AP///wD///8A///4AB//+AAf//gAH//4AB//wAAD/8AAA//AAAP/wAAD/gAAAH4AAAB+AAAAfgAAAHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAMAAAAAAAAAB4AAAAAAAAAHgAAAAAABgAeAAAAAAAAADwAAAAAAAYAFhgAAAAAAAHcAA4AAwZGADYYAAAHHAABwAAfAB8PxgA2HyAADz7AA94AH4CfjMYAMxswABs68AG8ABmMmQzGDiMZvBwYMvsA/QAZjJgMxh4/Gb4+GDP/g/wAMIyYDMYTPxmzNBgzz4B8ADCMmAzGN3sZszAZM8yDxQAwDJgExj5jmbM8GxPMgdwAM4yYB8YwYZ+zHh8fzMHdADPN2AfGMmAfswbMDszB3QARz9gAxjZgGzsmwADMwZ0AGY6ADMYeABg/PIAATMWdAB+AAATCGAAYNzgAAAzBnQAPgAAHwAAAGDAAAAAAxZ0ABwAAA8AAAAAwAAAAAA2cAAAAAAAAAAAAMAAAAAABgDgAAAH4AAAB+BAAAfgAAAH/AAAP/wAAD/8AAA//AAAP//AA///wAP//8AD///AA///+B////gf///4H///+B//'
logoPongB = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHw/n5+DwAAAAAAAAAAAAADuf44fjGAAAAAAAAAAAAAAw2AEGGwwAAAAAAAAAAAAAMdgBBjMMAAAAAAAAAAAAAD4fAQfDDAAAAAAAAB////A6GAEGgwwB////AAAQ///QMZ/hBmOcAT///QAAEAAAEBCAAAAQ8AEAAAAAABAAAAAAAAAAAAABAAABAAAT//+QAAADwAAAAR//+AAAE3d9gAAAA8AAAAEXN/gAABM3fYAAAAAAAAABEzfZAAATs2WAABgAAAAAARs22AAAE/t9gAAAAAAAAAEft9gAABP/fYD8ARn+wH4BHDfYAAAR//+QwyCxgEBgAR//+AAAEAAAAMMg4YBAMAEAAAAAABb89vD+IOGgQAwBp+8vAAAe//74wCGxgEACAW//54AAH///+MAhkYBAAwH///+AAB////jAIxn+fnwB////gAAwAAAIAAAAAAAAAQAAAIAAMAAACAAAAAAAAAEAAACAADAAAAgAAAAAAAABAAAAgAAwAAAIAAAAAAAAAQAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
logoPongIB = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/B4YYfgPgcMM/wAAAAAAAMdxnmYAOAwz/MAAAAAAAAD8YZnmeDHv83z+AAAAAAAAwGGY5jgw7DMMwAAAAAAAAMAeGGH4D+wzDP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAH//////5n//////4AAAAABgAAAAAAYAAAAAAOAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYA/wAAAGAAAA/wBgAAAAAGA//AAABgAAB//AYAAAAABg//8AAAYAAB//8GAAAAAAYP//gAAGDgAf//BgAAAAAGD//wAABj+AH//wYAAAAABg//8AAAY/gB//8GAAAAAAYP//AAAGDgAP//BgAAAAAGAf+AAABgAAAf+AYAAAAABgD/AAAAYAAAH/AGAAAAAAYAMAAAAGAAAAIABgAAAAAGADwAAABgAAADwAYAAAAABgA8AAAAYAAAA8AGAAAAAAYAPAAAAGAAAAPABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAAB//////8Z//////+AAAAAAf//////mf//////gAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAADoAAAAAGAAAAAAwAAAAAAA+AAAAABgAAAAAfAAAAAAAIAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4AMMAAAMAAAMAAMHgAAAAGADDAAADAAADAADBtu488B7t987YB84A985v8bO7ccAbbMMbbAMbAcMbOsHjHzzwG2zDG2wDGwDzDzDBgxgOOBts23tsA3sAO3sw2cePffA+PnHObAHOAfHf+HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
clean_count = 0
analog_min = 22000
analog_max = 51000
paddle_l_y_old = -1
paddle_r_y_old = -1
max_score = 10
ball_speed = 6
ball_width = 3
ball_height = 3
ball_half_height = ball_height >> 1
ball_x = 0
ball_y = 0
ball_vx = ball_speed
ball_vy = ball_speed
max_x = 128
max_y = 64
min_x = 0
min_y = 0
paddle_width = 3
paddle_height = 12
paddle_half_height = paddle_height >> 1
paddle_x = 128 - paddle_width
paddle_y = 30
paddle_speed = 5
net_width = 2
net_segmment_height = 5
net_segmment_gap = 3
l_score = 0
r_score = 0
last_up = time.ticks_ms()


def play_theme():
    notes = [[587,0.5],[523,0.5],[587,0.5],[0,0.5],[587,0.5],[523,0.5],[587,0.5],[0,0.5]
             ,[587,0.5],[523,0.5],[440,0.5],[523,0.5],[659,0.5],[523,0.5],[587,0.75]]
    for note in notes:
        speaker.duty_u16(int(65535/2))
        if note[0] == 0:
            speaker.duty_u16(0)
        else:
            speaker.freq(note[0])
        time.sleep(note[1])
    speaker.duty_u16(0)

def draw_net(d):
    y=0
    while y < max_y:
        d.fill_rect((max_x-net_width)>>1,y,net_width,net_segmment_height,1)
        y+=net_segmment_height + net_segmment_gap

def roundUp(x):
    return ((x+7)&(-8))


def customToBuff(data):
    width = data[0]
    height = data[1]
    fbuff = framebuf.FrameBuffer(data[2:],width,height, framebuf.MONO_HLSB)
    return fbuff
      
    
"""
Change value of analog pin to y position
"""
def analog_to_y(analog_pin):
    analog = analog_pin.read_u16()
    if analog < analog_min:
        analog = analog_min
    if analog > analog_max:
        analog = analog_max
    analog = analog - analog_min
    analog = analog / (analog_max - analog_min)
    analog= int(analog * (max_y - paddle_height))
    return analog

def sound_miss():
    speaker.duty_u16(int(65535/2))
    speaker.freq(220)
    timer = machine.Timer()
    timer.init(freq=2, mode=machine.Timer.ONE_SHOT, callback=sound_off)
    
def sound_hit():
    speaker.duty_u16(int(65535/2))
    speaker.freq(440)
    timer = machine.Timer()
    timer.init(freq=20, mode=machine.Timer.ONE_SHOT, callback=sound_off)
    
def sound_bounce():
    speaker.duty_u16(int(65535/2))
    speaker.freq(330)
    timer = machine.Timer()
    timer.init(freq=20, mode=machine.Timer.ONE_SHOT, callback=sound_off)

def sound_off(timer):
    speaker.duty_u16(0)

def point_to(player):
    pass
    
def intro():
    global l_score, r_score
    display.clear()
    display.showShape(logoPong)
    time.sleep(5)
    display.showShape(logoPongI)
    time.sleep(10)
    
def play_frame():
    pass

logoSmallBuff = customToBuff(bytearray(base64.b64decode(logoSmallB)))
logoLargeBuff = customToBuff(bytearray(base64.b64decode(logoLargeB)))
logoPong = customToBuff(bytearray(base64.b64decode(logoPongB)))
logoPongI = customToBuff(bytearray(base64.b64decode(logoPongIB)))

while True:
    if mode == mode_playing:
        play_frame()
    elif mode == mode_init:
        intro()
        mode = mode_playing
    elif mode == mode_game_over:
        time.sleep(0.1)
        if play_button.value():
            intro()
            mode=mode_playing
    



