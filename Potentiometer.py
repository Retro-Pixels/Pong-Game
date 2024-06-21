import machine

"""
This class is very specific for the pong game and will not work on other application without
previous modifications
"""

class Potentiometer:
    def __init__(self, pin):
        self._pot = machine.ADC(pin)
        self._pin = pin

    def analog_to_digital(self, analog_min = 22000, analog_max = 51000, max_y=64, paddle_height=12):
        analog = self._pot.read_u16()
        if analog < analog_min:
            analog = analog_min
        if analog > analog_max:
            analog = analog_max
        analog = analog - analog_min
        analog = analog / (analog_max - analog_min)
        analog= int(analog * (max_y - paddle_height))
        return analog