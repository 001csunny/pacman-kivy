from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class Player(Widget):
    pac_img = StringProperty('img/boy_right.gif')
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        
        self.pos = Vector(*self.velocity)+self.pos
        
        if self.velocity == [0, 1]:
            self.pac_img = "img/boy_up.gif"
        elif self.velocity == [0, -1]:
            self.pac_img = "img/boy_down.gif"
        elif self.velocity == [-1, 0]:
            self.pac_img = "img/boy_left.gif"
        elif self.velocity == [1, 0]:
            self.pac_img = "img/boy_right.gif"