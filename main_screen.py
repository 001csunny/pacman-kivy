from kivy.config import Config
Config.set("graphics", "resizable", False)

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,FallOutTransition
from main import *
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Window.size = (1200,400)

# if window size bugged use this size instead
Window.size = (960, 320)

Builder.load_string(
    """
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    Button:
        pos: 357,147
        on_press: root.manager.current_screen.add_widget(root.gaming.build())
"""
)


# Declare both screens
class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    gaming = PacmanApp()
    gaming.load_kv()


class MainScreenApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        men = SettingsScreen(name="settings")
        sm.add_widget(men)
        return sm


if __name__ == "__main__":
    MainScreenApp().run()
