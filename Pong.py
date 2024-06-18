from Buzzer import PassiveBuzzer
from Button import *
from GraphicDisplay import *
from Potentiometer import *

RetroPixlsLogo = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHw/n5+DwAAAAAAAAAAAAADuf44fjGAAAAAAAAAAAAAAw2AEGGwwAAAAAAAAAAAAAMdgBBjMMAAAAAAAAAAAAAD4fAQfDDAAAAAAAAB////A6GAEGgwwB////AAAQ///QMZ/hBmOcAT///QAAEAAAEBCAAAAQ8AEAAAAAABAAAAAAAAAAAAABAAABAAAT//+QAAADwAAAAR//+AAAE3d9gAAAA8AAAAEXN/gAABM3fYAAAAAAAAABEzfZAAATs2WAABgAAAAAARs22AAAE/t9gAAAAAAAAAEft9gAABP/fYD8ARn+wH4BHDfYAAAR//+QwyCxgEBgAR//+AAAEAAAAMMg4YBAMAEAAAAAABb89vD+IOGgQAwBp+8vAAAe//74wCGxgEACAW//54AAH///+MAhkYBAAwH///+AAB////jAIxn+fnwB////gAAwAAAIAAAAAAAAAQAAAIAAMAAACAAAAAAAAAEAAACAADAAAAgAAAAAAAABAAAAgAAwAAAIAAAAAAAAAQAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
PongGameLogo = b'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/B4YYfgPgcMM/wAAAAAAAMdxnmYAOAwz/MAAAAAAAAD8YZnmeDHv83z+AAAAAAAAwGGY5jgw7DMMwAAAAAAAAMAeGGH4D+wzDP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAH//////5n//////4AAAAABgAAAAAAYAAAAAAOAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYA/wAAAGAAAA/wBgAAAAAGA//AAABgAAB//AYAAAAABg//8AAAYAAB//8GAAAAAAYP//gAAGDgAf//BgAAAAAGD//wAABj+AH//wYAAAAABg//8AAAY/gB//8GAAAAAAYP//AAAGDgAP//BgAAAAAGAf+AAABgAAAf+AYAAAAABgD/AAAAYAAAH/AGAAAAAAYAMAAAAGAAAAIABgAAAAAGADwAAABgAAADwAYAAAAABgA8AAAAYAAAA8AGAAAAAAYAPAAAAGAAAAPABgAAAAAGAAAAAABgAAAAAAYAAAAABgAAAAAAYAAAAAAGAAAAAAYAAAAAAGAAAAAABgAAAAAGAAAAAABgAAAAAAYAAAAAB//////8Z//////+AAAAAAf//////mf//////gAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAADoAAAAAGAAAAAAwAAAAAAA+AAAAABgAAAAAfAAAAAAAIAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4AMMAAAMAAAMAAMHgAAAAGADDAAADAAADAADBtu488B7t987YB84A985v8bO7ccAbbMMbbAMbAcMbOsHjHzzwG2zDG2wDGwDzDzDBgxgOOBts23tsA3sAO3sw2cePffA+PnHObAHOAfHf+HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'


class PongGame:
    def __init__(self):
        
        self._analog_pin_left = machine.ADC(26)
        self._analog_pin_right = machine.ADC(27)
        self._buz = PassiveBuzzer(16)
        self._buttons = [
            Button(22, '1P', buttonhandler=None),
            Button(21, '2P', buttonhandler=None)
        ]

    def stateDo(self, state):
        print(f"Executing stateDo for state {state}")
        if state == 0:
            self._melody.play_melody(zelda_melody)
        elif state == 3:
            self._melody.play_melody(zeldas_lullaby)

    def stateEntered(self, state, event):
        print(f"Entering state {state} due to event {event}")
        if state == 0:
            self._display.blit(_discustomTobuff(), 0, 2)
        elif state == 1:
            self.refresh()
            self._display.showText(' ' * 16, 1, 0)  # Clear display
            self._playing = True
            self.check_game_over()  # Check if the game is over when entering state 1
        elif state == 2:
            self.check_match(event)
            self._model.gotoState(1)  # Return to game play state after checking match
        elif state == 3:
            self._playing = False
            self._display.showText('   GAME OVER!   ', 1, 0)
            time.sleep(3)
            self._lights.run(2)  # Run light animation

    def stateLeft(self, state, event):
        print(f"Exiting state {state} due to event {event}")
        if state == 0:
            self._melody.stop()  # Stop the melody if the state is exited
        elif state == 3:
            self._melody.stop()
            self.reset_game_field()
            self._lights.off()
