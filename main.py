from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class Vimoweb(MDApp):
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("intro.kv"))
        sm.add_widget(Builder.load_file("home.kv"))
        return sm
    
    def on_start(self):
        Clock.schedule_once(self.change_screen, 3)

    def change_screen(self, dt):
        sm.current = "HomeScreen"

if __name__ == '__main__':
    Vimoweb().run()
