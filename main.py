from kivy.config import Config

Config.set("graphics", "resizable", False)

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from player import *

Window.size = (1200,400)

# if window size bugged use this size instead
#Window.size = (960, 320)


class GamePlay(Screen):
    ps = NumericProperty(77)
    ww = NumericProperty(1200)
    wh = NumericProperty(400)

    def on_size(self, *args):
        print("Window size:", self.width, self.height)

    def on_touch_move(self, touch):
        print("ตำแหน่งหน้าต่าง:", Window.mouse_pos)
        
    pacman = Player()


class Wall(Widget):
    pass


class PacmanApp(App):
    def build(self):
        return GamePlay()


if __name__ == "__main__":
    PacmanApp().run()
