from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.animation import Animation
from math import cos, sin, pi
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
import requests

KV = '''
MDScreen:
    MDBottomNavigation:
        selected_color_background: "orangered"
        text_color_active: "orangered"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'home'
            MDFloatLayout:
                MDIconButton:
                    id: main_button
                    icon: "lightning-bolt-outline"
                    md_bg_color: "orangered"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    on_release: app.toggle_sub_buttons()
    
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'console'
            icon: 'console-line'
            MDLabel:
                text: 'Console'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Database'
            icon: 'database'
            MDLabel:
                text: 'Database'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Settings'
            icon: 'cog'
            MDLabel:
                text: 'Settings'
                halign: 'center'
'''

class Vimoweb(MDApp):
    output_label = None  # Class attribute to store the output label

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def toggle_sub_buttons(self):
        main_button = self.root.ids.main_button
        if main_button.icon == "lightning-bolt-outline":
            self.create_sub_buttons()
            main_button.icon = "close-circle-outline"
        else:
            # Clear sub-buttons and change the main button icon to default
            self.clear_sub_buttons()
            main_button.icon = "lightning-bolt-outline"

    def sub_button_callback(self, instance):
        print(f"Sub-button {instance.icon} pressed!")

        if instance.icon == "ip":
            self.clear_sub_buttons()
            main_button = self.root.ids.main_button
            main_button.parent.remove_widget(main_button)
            input_text = MDTextField(
                id="input_text",
                hint_text="IP Address",
                pos_hint={"center_x": 0.5, "center_y": 0.8},
                size_hint_x=0.5
            )

            submit_button = MDRaisedButton(
                text="Get",
                pos_hint={"center_x": 0.5, "center_y": 0.7},
            )
            submit_button.bind(on_release=lambda instance: self.ipsearch(input_text.text))  # Pass the text value

            self.output_label = MDLabel(
                id="output_label",
                text="",
                halign="center",
                
                pos_hint={"center_x": 0.5, "center_y": 0.4},
                text_color = "gold"
                
            )
                
            self.root.add_widget(input_text)
            self.root.add_widget(submit_button)
            self.root.add_widget(self.output_label)

    def ipsearch(self, text_value):
        try:
            # Fetch the public IP address using the ipinfo.io API
            url = f'https://ipinfo.io/{text_value}/json'
            response = requests.get(url)
            data = response.json()

            # Extract and return relevant details
            ip_address = data.get('ip', 'N/A')
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            country = data.get('country', 'N/A')
            location = data.get('loc', 'N/A')

            ip_details = {
                'IP Address' : ip_address,
                'City' : city,
                'Region' : region,
                'Country' : country,
                'Location' : location
            }
            print(ip_details)
            formatted_details = "\n".join(f"{key} : {value}" for key, value in ip_details.items())

            # Set the text property
            self.output_label.text = formatted_details
            return ip_details

        except Exception as e:
            # Handle exceptions (e.g., network issues, API errors)
            print(f"Error fetching IP details: {e}")
            return None

    def create_sub_buttons(self):
        # Clear existing sub-buttons
        self.clear_sub_buttons()

        num_buttons = 6
        angle_increment = 2 * pi / num_buttons
        radius = 100  # Change this value for a shorter radius
        center_x, center_y = self.root.width / 2, self.root.height / 2

        main_button = self.root.ids.main_button

        # List of different icons for sub-buttons
        icons = ["ip", "phone", "wifi", "instagram", "facebook", "web"]

        for i in range(num_buttons):
            angle = i * angle_increment
            x = center_x + radius * cos(angle)
            y = center_y + radius * sin(angle)

            # Use icons cyclically
            icon_index = i % len(icons)
            sub_button = MDIconButton(
                icon=icons[icon_index],
                md_bg_color="orangered",
                pos=(main_button.center_x - 25, main_button.center_y - 25),
                size_hint=(None, None),
            )
            sub_button.bind(on_release=self.sub_button_callback)  # Bind the callback function
            self.root.add_widget(sub_button)

            # Animation for each sub-button
            anim = Animation(pos=(x - 30, y + 10), duration=0.5)
            anim.start(sub_button)

    def clear_sub_buttons(self):
        # Clear existing sub-buttons
        for child in self.root.children[:]:
            if isinstance(child, MDIconButton) and child != self.root.ids.main_button:
                self.root.remove_widget(child)

if __name__ == '__main__':
    Vimoweb().run()
