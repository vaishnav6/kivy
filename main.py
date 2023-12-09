from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.imagelist import *

KV = '''
<MobileView>
    BoxLayout:
        orientation: 'vertical'

        AsyncImage:
            source: 'images\lion.png' 
            size_hint_y: 0.7 
        
<TabletView>
    BoxLayout:
        orientation: 'vertical'

        AsyncImage:
            source: 'images\lion.png' 
            size_hint_y: 0.7
            
<DesktopView>
    BoxLayout:
        orientation: 'vertical'

        AsyncImage:
            source: 'images\lion.png' 
            size_hint_y: 0.7

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


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


Test().run()
