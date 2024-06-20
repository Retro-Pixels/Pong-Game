from GraphicDisplay import OLED

class PlayingField(OLED):
    def __init__(self, sda=0, scl=1, i2cid=0, width=128, height=64):
        super().__init__(sda, scl, i2cid, width, height)

    def draw_net_scores(self,l_score, r_score, net_segmment_height=5, net_segmment_gap=3, net_width=2, max_x=128, max_y=64):
        y=0
        while y<max_y:
            self._buff.fill_rect((max_x-net_width)>>1,y,net_width,net_segmment_height,1)
            y+=net_segmment_height + net_segmment_gap

        self._buff.text(str(l_score),30,0,1)
        self._buff.text(str(r_score),90,0,1)
        self._display.blit(self._buff, 0, 0)
        self._display.show()
