import ssd1306
import machine
import utime as time
import framebuf
import base64
import math

class OLED:
    def __init__(self, sda=0, scl=1, i2cid=0, width=128, height=64):
        i2c = machine.I2C(i2cid,sda=machine.Pin(sda),scl=machine.Pin(scl))
        self._display = ssd1306.SSD1306_I2C(width,height,i2c)
        self._buff = framebuf.FrameBuffer(bytearray(width*height),width,height,framebuf.MONO_HLSB)

    def customTobuff(self, data):
        buffData = bytearray(base64.b64decode(data))

    def showShape(self, data, row, col):
        self._display.blit(data,row, col)
    
    def showText(self,text, x=0, y=0, color=1):
        self._buff.text(text, x, y, color)
        self._display.blit(self._buff, 0, 0)