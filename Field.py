#from GraphicDisplay import OLED
import machine
import ssd1306
import framebuf
import base64
class PlayingField:
    def __init__(self, sda=0, scl=1, i2cid=0, width=128, height=64):
        i2c = machine.I2C(i2cid, sda=machine.Pin(sda), scl=machine.Pin(scl))
        self._display = ssd1306.SSD1306_I2C(width, height, i2c)
        self._buff = framebuf.FrameBuffer(bytearray(width * height), width, height, framebuf.MONO_HLSB)

    def customToBuff(self, data):
        databyte = bytearray(base64.b64decode(data))
        width = databyte[0]
        height = databyte[1]
        fbuff = framebuf.FrameBuffer(databyte[2:], width, height, framebuf.MONO_HLSB)
        return fbuff

    def clear(self):
        self._display.fill(0)
        self._display.show()

    def draw_net_scores(self, l_score, r_score, net_segment_height=5, net_segment_gap=3, net_width=2, max_x=128, max_y=64):
        y = 0
        while y < max_y:
            self._buff.fill_rect((max_x - net_width) >> 1, y, net_width, net_segment_height, 1)
            y += net_segment_height + net_segment_gap

        self._buff.text(str(l_score), 30, 0, 1)
        self._buff.text(str(r_score), 90, 0, 1)
        self._display.blit(self._buff, 0, 0)

    def draw_paddle(self, paddle, color, pos, paddle_height=12, paddle_width=3):
        self._display.fill_rect(pos, paddle, paddle_width, paddle_height, color)

    def draw_ball(self, ball_x, ball_y, color, ball_width=3, ball_height=3):
        self._display.fill_rect(int(ball_x), int(ball_y), ball_width, ball_height, color)

    def draw_score(self, score, pos, color=1):
        self._buff.fill_rect(pos, 0, 20, 8, 0)
        self._buff.text(str(score), pos, 0, color)
    
    def showShape(self, data, row=0, col=0):
        self._display.fill(0)
        self._display.blit(data, row, col)
        self._display.show()

    def showText(self, text, x=0, y=0, color=1):
        self._buff.text(text, x, y, color)
        self._display.blit(self._buff, 0, 0)
        self._display.show()
    
    def addToBuffer(self):
        self._display.blit(self._buff, 0, 0)
        
    def show(self):
        self._display.show()
