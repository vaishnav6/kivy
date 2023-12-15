from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.imagelist import *
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime


KV = '''
<MobileView>
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
            on_release: app.on_get_started_button_click(self)

<TabletView>
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
            on_release: app.on_get_started_button_click(self)

<DesktopView>
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
            on_release: app.on_get_started_button_click(self)
<HomeScreen>
    FloatLayout:
        MDLabel:
            id: datetime_label
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0.5, 1, 1
            font_style: "H6"
            bold: True
            pos_hint: {'center_x': 0.9, 'center_y': 0.9}

ResponsiveView:
'''


class CommonComponentLabel(MDLabel):
    pass


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass

class HomeScreen(MDScreen):
    pass

class ResponsiveView(ScreenManager):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView(name='mobile_view')
        self.tablet_view = TabletView(name='tablet_view')
        self.desktop_view = DesktopView(name='desktop_view')
        self.home_screen = HomeScreen(name='home_screen')
        self.add_widget(self.mobile_view)
        self.add_widget(self.tablet_view)
        self.add_widget(self.desktop_view)
        self.add_widget(self.home_screen)

    

class Vimoweb(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_get_started_button_click(self, instance):
        # Disable the button during screen transition
        instance.disabled = True

        # Change the current screen to the home screen
        self.root.current = 'home_screen'
        datetime_label = self.root.get_screen('home_screen').ids.datetime_label
        current_datetime = datetime.now()

        # Format the datetime object
        formatted_date = current_datetime.strftime("%d/%m/%Y")
        formatted_time = current_datetime.strftime("%I:%M %p")

        datetime_label.text = f"{formatted_time}\n{formatted_date}"


Vimoweb().run()
