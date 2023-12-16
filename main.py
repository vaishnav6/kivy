from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import *
from kivy.metrics import dp

KV = '''
WindowManager:
    IntroWindow:
    HomeWindow:

<IntroWindow>:
    name: "intro"
    FloatLayout:
        AsyncImage:
            source: 'https://i.ibb.co/rHFY8Hp/logo-removebg-preview.png' 
            size_hint_y: 0.7
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}

        MDRectangleFlatButton:
            text: "Get Started"
            adaptive_size: True
            md_bg_color: "gold"
            text_color: "#202020"
            font_weight: "bold"
            elevation_hover: 4
            pos_hint: {'center_x': 0.5, 'center_y': 0.22}
            on_release: app.on_started_button_click(self)

<HomeWindow>:
    name: "home"
    FloatLayout:
        RoundMenuButton:
            id: round_menu_button
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.menu.open()


<RoundMenuButton@MDFloatingActionButton>:
    icon: "lightning-bolt-outline"
    size: dp(56), dp(56)
    elevation_normal: 8
    elevation_hover: 12
    md_bg_color: "orangered"
    on_release: app.menu.open()
'''

class IconListItem(OneLineIconListItem):
    icon = "dots-vertical"

class IntroWindow(Screen):
    pass

class HomeWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Vimoweb(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_started_button_click(self, instance):
        self.root.current = "home"
        self.root.transition.direction = "up"

        menu_items = [
            {
                "viewclass": "IconListItem",
                "text": "IP",
                "height": dp(56),
                "on_release": lambda x="IP": self.set_menu_item(x),
            },
            {
                "viewclass": "IconListItem",
                "text": "Facebook",
                "height": dp(56),
                "on_release": lambda x="Facebook": self.set_menu_item(x),
                
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.get_screen('home').ids.round_menu_button,
            items=menu_items,
            position="center",
            width_mult=4,
        )

    def set_menu_item(self, text_item):
        # Update the label text here
        print(f"Selected item: {text_item}")
        self.menu.dismiss()

if __name__ == "__main__":
    Vimoweb().run()
