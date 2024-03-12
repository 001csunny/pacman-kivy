from kivy.config import Config

Config.set("graphics", "resizable", False)

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from original_pacman.main import *
from kivy.properties import NumericProperty, StringProperty
from kivy.app import App
from kivy.core.audio import SoundLoader
import original_pacman.setting as setting

Window.size = (1200,400)

# if window size bugged use this size instead
#Window.size = (960, 320)

menu_sound = SoundLoader.load('menu_bg_song.mp3')
menu_sound.play()
menu_sound.volume = 0.5

Builder.load_string(
    """
<MenuScreen>:
    FloatLayout:
        Image:
            id:'pacman'
            source: root.img
        Button:
            size_hint: 0.2,0.2
            pos: (root.ww/2)-20,(root.wh/2)-240
            text: 'Start Game'
            on_press: root.manager.current_screen.add_widget(root.gaming.build());
        Button:
            size_hint: 0.2, 0.1
            pos: (root.ww/2)-20,(root.wh/2)
            text: 'Settings'
            on_press: root.manager.current = 'settings'
        Slider:
            id: slider
            size_hint: 0.3,0.5
            pos: (root.ww/2)-80,-80
            value: 0.5
            min: 0
            max: 1 
            on_value: root.update_volume(slider.value)
        Label:
            text: '{:.0f}'.format(slider.value * 100)
            pos: 0, -120
"""
)

Builder.load_string(
    """
<SettingsScreen>:
    FloatLayout:
        Image:
            source: root.img
        Button:
            size_hint: 0.3, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            text: '<-- Back to Menu'
            on_press: root.manager.current = 'menu'
        Button:
            size_hint: 0.3, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            text: 'Model 1'
            on_press: root.callback("img/boy")
        Button:
            size_hint: 0.3, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            text: 'Model 2'
            on_press: root.callback("img/pac")
"""
)

class SettingsScreen(Screen):
    img = StringProperty("img/setting.png")
    model_selected = ''
    def callback(self, text):
        self.model_selected = text
        print(f'{text}')
    setting.model = model_selected

class MenuScreen(Screen):
    img = StringProperty("img/menu.png")
    ww = NumericProperty(Window.size[0])
    wh = NumericProperty(Window.size[1])
    gaming = PacmanApp()
    gaming.load_kv()

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