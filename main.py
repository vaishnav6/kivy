from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class Vimoweb(MDApp):
    current_index = 0
    text_to_type = "VIMOWEB"
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("intro.kv"))
        sm.add_widget(Builder.load_file("home.kv"))
        return sm
    
    def on_start(self):
        Clock.schedule_interval(self.typing, 0.2)
        Clock.schedule_once(self.change_screen, 4)

    def change_screen(self, dt):
        sm.current = "HomeScreen"

    def typing(self, *args):
        if self.current_index < len(self.text_to_type):
            current_text = sm.get_screen("IntroScreen").ids.typings.text
            current_text += self.text_to_type[self.current_index]
            sm.get_screen("IntroScreen").ids.typings.text = current_text
            self.current_index += 1

if __name__ == '__main__':
    Vimoweb().run()
