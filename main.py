from kivy.config import Config

Config.set("graphics", "resizable", False)

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from player import *
from kivy.clock import Clock

# Window.size = (1200,400)

# if window size bugged use this size instead
Window.size = (960, 320)


class GamePlay(Screen):
    ps = NumericProperty(77)
    ww = NumericProperty(1200)
    wh = NumericProperty(400)


    def on_size(self, *args):
        print("Window size:", self.width, self.height)

    def on_touch_move(self, touch):
        print("ตำแหน่งหน้าต่าง:", Window.mouse_pos)
        
    pacman = Player()
    
    def __init__(self, **kwargs):
        super(GamePlay,self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            self.pacman.velocity=(0,1)
        elif keycode[1] == 'down':
            self.pacman.velocity=(0,-1)
        elif keycode[1] == 'left':
            self.pacman.velocity=(-1,0)
        elif keycode[1] == 'right':
            self.pacman.velocity=(1,0)

        return True
    
    def update(self, dt):
        self.pacman.move()
        
class Wall(Widget):
    pass


class PacmanApp(App):
    def build(self):
        game = GamePlay()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    PacmanApp().run()
