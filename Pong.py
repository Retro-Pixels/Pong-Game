from GraphicDisplay import *
from Field import *
from StateModel import *
from Counters import SoftwareTimer
from Melody import *
from Button import *

class PongGame:
    def __init__(self):


        self.RetroPixlsLogo = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHw/n5+DwAAAAAAAAAAAAADuf44fjGAAAAAAAAAAAAAAw2AEGGwwAAAAAAAAAAAAAMdgBBjMMAAAAAAAAAAAAAD4fAQfDDAAAAAAAAB////A6GAEGgwwB////AAAQ///QMZ/hBmOcAT///QAAEAAAEBCAAAAQ8AEAAAAAABAAAAAAAAAAAAABAAABAAAT//+QAAADwAAAAR//+AAAE3d9gAAAA8AAAAEXN/gAABM3fYAAAAAAAAABEzfZAAATs2WAABgAAAAAARs22AAAE/t9gAAAAAAAAAEft9gAABP/fYD8ARn+wH4BHDfYAAAR//+QwyCxgEBgAR//+AAAEAAAAMMg4YBAMAEAAAAAABb89vD+IOGgQAwBp+8vAAAe//74wCGxgEACAW//54AAH///+MAhkYBAAwH///+AAB////jAIxn+fnwB////gAAwAAAIAAAAAAAAAQAAAIAAMAAACAAAAAAAAAEAAACAADAAAAgAAAAAAAABAAAAgAAwAAAIAAAAAAAAAQAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        self.PongGameLogo = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/B4YYfgPgcMM/wAAAAAAAMdxnmYAOAwz/MAAAAAAAAD8YZnmeDHv83z+AAAAAAAAwGGY5jgw7DMMwAAAAAAAAMAeGGH4D+wzDP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAH//////5n//////4AAAAABgAAAAAAYAAAAAAOAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYA/wAAAGAAAA/wBgAAAAAGA//AAABgAAB//AYAAAAABg//8AAAYAAB//8GAAAAAAYP//gAAGDgAf//BgAAAAAGD//wAABj+AH//wYAAAAABg//8AAAY/gB//8GAAAAAAYP//AAAGDgAP//BgAAAAAGAf+AAABgAAAf+AYAAAAABgD/AAAAYAAAH/AGAAAAAAYAMAAAAGAAAAIABgAAAAAGADwAAABgAAADwAYAAAAABgA8AAAAYAAAA8AGAAAAAAYAPAAAAGAAAAPABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAAB//////8Z//////+AAAAAAf//////mf//////gAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAADoAAAAAGAAAAAAwAAAAAAA+AAAAABgAAAAAfAAAAAAAIAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4AMMAAAMAAAMAAMHgAAAAGADDAAADAAADAADBtu488B7t987YB84A985v8bO7ccAbbMMbbAMbAcMbOsHjHzzwG2zDG2wDGwDzDzDBgxgOOBts23tsA3sAO3sw2cePffA+PnHObAHOAfHf+HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

        self.l_score = 0
        self.r_score = 0
        self.clean_count = 0

        self._display = OLED()  
        self._field = PlayingField()
        self._buzz = PassiveBuzzer(17)
        self._melody = Melody(17)
        self._buttons = [
            Button(22, '1P', buttonhandler=None),
            Button(21, '2P', buttonhandler=None)
        ]

        self._model = StateModel(5, self, debug=True)
        for button in self._buttons:
            self._model.addButton(button)
        self._timer = SoftwareTimer(None)
        self._model.addTimer(self._timer)

        # Define transitions
        self._model.addTransition(0, [BTN1_PRESS], 1)
        self._model.addTransition(0, [BTN2_PRESS], 2)
        self._model.addTransition(4, [BTN1_PRESS, BTN2_PRESS], 0)

        # Run the state model
        self._model.run()
        

    def stateDo(self, state):
        print(f"Executing stateDo for state {state}")
        if state == 0:
            #self._melody.play_melody(zelda_melody)
            self._melody.play_melody(40) # On Pico is a numbered convention on wowki it would be zelda_melody
        elif state == 3:
            #self._melody.play_melody(zelda_lullaby)
            self._melody.play_melody(39) ## On Pico is a numbered convention on wowki it would be zelda_lullaby

    def stateEntered(self, state, event):
        print(f"Entering state {state} due to event {event}")
        if state == 0:
            self.titleScreen()
        elif state == 1:
            pass
        elif state == 2:
            pass
        elif state == 3:
            pass

    def stateLeft(self, state, event):
        print(f"Exiting state {state} due to event {event}")
        if state == 0:
            self._display.clear()
            self.l_score = 0
            self.r_score = 0
            self._field.draw_net_scores(self.l_score, self.r_score)
            self.clean_count = 0
            self._melody.stop()  # Stop the melody if the state is exited
        elif state == 3:
            pass


    def titleScreen(self):
        self._display.clear()

        RetroPixlsBuffer = self._display.customToBuff(self.RetroPixlsLogo)
        PongGameBuffer = self._display.customToBuff(self.PongGameLogo)

        self._display.showShape(RetroPixlsBuffer, 0, 2)
        time.sleep(5)

        self._display.showShape(PongGameBuffer, 0, 2)


        """self._display.clear()
        self.l_score = 0
        self.r_score = 0
        field.draw_net_scores(l_score, r_score)
        clean_count = 0"""


if __name__ == '__main__':
    game = PongGame()
    while True:
        time.sleep(0.1)
        game._model.run()
