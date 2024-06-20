import ssd1306
import machine
import framebuf
import base64

class OLED:
    def __init__(self, sda=0, scl=1, i2cid=0, width=128, height=64):
        i2c = machine.I2C(i2cid, sda=machine.Pin(sda), scl=machine.Pin(scl))
        self._display = ssd1306.SSD1306_I2C(width, height, i2c)
        self._buff = framebuf.FrameBuffer(bytearray(width * height), width, height, framebuf.MONO_HLSB)

    def customToBuff(self, data):
        databyte = bytearray(base64.b64decode(data))
        width = databyte[0]
        height = databyte[1]
        fbuff = framebuf.FrameBuffer(databyte[2:],width,height, framebuf.MONO_HLSB)
        return fbuff

    def showShape(self, data, row=0, col=0):
        self._display.fill(0)
        self._display.blit(data, row, col)
        self._display.show()

    def showText(self, text, x=0, y=0, color=1):
        self._buff.text(text, x, y, color)
        self._display.blit(self._buff, 0, 0)
        self._display.show()

    def clear(self):
        self._display.fill(0)
        self._display.show()

