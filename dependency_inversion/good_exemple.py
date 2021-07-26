from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    
    def turn_on(self):
        pass

    @abstractmethod  
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb : Turned on...")

    def turn_off(self):
        print("LightBulb : Turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan : Turned on...")

    def turn_off(self):
        print("Fan : Turned off...")

class ElectricPowerSwitch:

    def __init__(self, s: Switchable) -> None:
        self.switchable = s
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True

l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
switch.press()
switch.press()
switch.press()