from kivy.config import Config

Config.set("graphics", "resizable", False)

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager, FallOutTransition
from main import *
from kivy.properties import NumericProperty, StringProperty
# from kivy.uix.popup import Popup
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label

# Window.size = (1200,400)

# if window size bugged use this size instead
Window.size = (960, 320)

Builder.load_string(
    """
<MenuScreen>:
    FloatLayout:
        Image:
            id:'pacman'
            source: root.img
        Button:
            size_hint: 0.2,0.2
            pos: (root.ww/2)-20,(root.wh/2)-220
            text: 'Start Game'
            on_press: root.manager.current_screen.add_widget(root.gaming.build()) ; 
"""
)

class MenuScreen(Screen):
    img = StringProperty('img/menu.png')
    ww = NumericProperty(Window.size[0])
    wh = NumericProperty(Window.size[1])
    gaming = PacmanApp()
    gaming.load_kv()



class MainScreenApp(App):
    def build(self):
        sm = ScreenManager(transition=FallOutTransition(duration=0.1))
        sm.add_widget(MenuScreen(name="menu"))
        return sm


if __name__ == "__main__":
    MainScreenApp().run()
