from kivy.config import Config

Config.set("graphics", "resizable", False)

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from player import *
from ghost import *
from food import *
from kivy.clock import Clock
from kivy.core.audio import SoundLoader


# Window.size = (1200,400)

# if window size bugged use this size instead
Window.size = (960, 320)

menu_sound = SoundLoader.load('bg_song.mp3')
menu_sound.play()

class GamePlay(Screen):
    ps = NumericProperty(77)
    ww = NumericProperty(1200)
    wh = NumericProperty(400)

    food_point = ['point{0}'.format(i) for i in range(0, len(food))]

    def on_size(self, *args):
        print("Window size:", self.width, self.height)

    def on_touch_move(self, touch):
        print("ตำแหน่งหน้าต่าง:", Window.mouse_pos)
        
    pacman = Player()
    ghost1 = Ghost()
    
    def __init__(self, **kwargs):
        super(GamePlay,self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        if keycode[1] == 'up':
            self.pacman.velocity=(0,1)
        elif keycode[1] == 'down':
            self.pacman.velocity=(0,-1)
        elif keycode[1] == 'left':
            self.pacman.velocity=(-1,0)
        elif keycode[1] == 'right':
            self.pacman.velocity=(1,0)
        elif keycode[1] == 'spacebar':
            self.pacman.velocity=(0,0)
            print(self.pacman.pos)
        
        return True
    
    def show_food(self):
        for i in range(0, len(food)):
            if i != 179 and 1 != 170:
                globals()[self.food_point[i]] = Points(pos=food[i], size = (5,5))
                self.add_widget(globals()[self.food_point[i]])
    
    def update(self, dt):
        self.pacman.move()

        for i in reversed(range(len(eaten))):
            if (self.pacman.pos[0] <= food[eaten[i]][0] - 20) and (
                self.pacman.pos[0] >= food[eaten[i]][0] - 50) \
                and (self.pacman.pos[1] <= food[eaten[i]][1] - 20) and (
                    self.pacman.pos[1] >= food[eaten[i]][1] - 50):
                self.remove_widget(globals()['point{0}'.format(eaten[i])])
                del eaten[i]
        
class Wall(Widget):
    pass


class PacmanApp(App):
    def build(self):
        game = GamePlay()
        game.show_food()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    PacmanApp().run()
