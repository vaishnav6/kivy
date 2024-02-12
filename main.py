from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (350,600)
LabelBase.register(name='lion', 
                   fn_regular='lion.ttf')
kv = """
<StartScreen>:
    name: 'start'
    MDFloatLayout:
        md_bg_color: "black"
        MDLabel:
            id: txt1
            text: "Hi"
            font_name: "lion"
            markup: True
            halign: "center"
            font_size: "30sp"
            opacity: 0
            color: "gold"
            bold: True

        MDLabel:
            id: txt2
            text: "VIMOWEB"
            font_name: "lion"
            halign: "center"
            font_size: "40sp"
            opacity: 0
            color: "gold"
            bold: True

<HomeScreen>:
    name: 'home'
    MDFloatLayout:
        md_bg_color: "black"
        MDLabel:
            text: "Home"
            halign: "center"
            font_size: "30sp"
            color: "white"
            font_name: "lion"
"""
class StartScreen(Screen):
    pass
class HomeScreen(Screen):
    pass


class Vimoweb(MDApp):
    id = 1

    def on_start(self):
        self.start()

    def start(self, *args):
        animation = Animation(opacity=1, duration=1) + \
                    Animation(opacity=1, duration=2) + \
                    Animation(opacity=0, duration=1)
        animation.bind(on_complete=self.start)

        current_screen = self.root.current_screen
        label_id = f"txt{self.id}"

        if label_id in current_screen.ids:
            animation.start(current_screen.ids[label_id])
        else:
            print(f"Label with ID {label_id} not found on the current screen.")

        sound = SoundLoader.load('intro.wav')
        if sound:
            sound.play()

        if self.id < 3:
            self.id += 1
        else:
            self.root.transition.direction = 'right'
            self.root.current = 'home'
            self.id = 1  

    def build(self):
        screen = Builder.load_string(kv)
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(HomeScreen(name='home'))

        return sm

if __name__ == "__main__":
    Vimoweb().run()
