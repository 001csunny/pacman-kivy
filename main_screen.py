from kivy.config import Config

Config.set("graphics", "resizable", False)

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from original_pacman.main import *
from easy_pacman.main import *
from kivy.properties import NumericProperty, StringProperty
from kivy.app import App
from kivy.core.audio import SoundLoader

# Window.size = (1200,400)

# if window size bugged use this size instead
Window.size = (960, 320)

menu_sound = SoundLoader.load('sound/menu_bg_song.mp3')
menu_sound.play()
menu_sound.volume = 0.5

class SettingsScreen(Screen):
    img = StringProperty("img/setting.png")
    ww = NumericProperty(Window.size[0])
    wh = NumericProperty(Window.size[1])

    def easy_mode(self):
        self.gaming = EasyPacmanApp()
        self.gaming.load_kv()

    def hard_mode(self):
        self.gaming = PacmanApp()
        self.gaming.load_kv()


class MenuScreen(Screen):
    img = StringProperty("img/menu.png")
    ww = NumericProperty(Window.size[0])
    wh = NumericProperty(Window.size[1])

    def update_volume(self, value):
        menu_sound.volume = value

class MainScreenApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition(duration=0.5))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(SettingsScreen(name="settings"))
        return sm

if __name__ == "__main__":
    MainScreenApp().run()
