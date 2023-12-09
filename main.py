# Import necessary modules
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.image import Image

class ImageCaptureApp(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical')

        # Create a Camera widget
        self.camera = Camera(resolution=(640, 480), play=True)
        layout.add_widget(self.camera)

        # Create buttons for capturing and viewing images
        capture_button = Button(text="Capture", size_hint_y=None, height=50)
        capture_button.bind(on_press=self.capture_image)
        layout.add_widget(capture_button)

        view_button = Button(text="View Image", size_hint_y=None, height=50)
        view_button.bind(on_press=self.view_image)
        layout.add_widget(view_button)

        # Create an Image widget for displaying captured images
        self.image_widget = Image()
        layout.add_widget(self.image_widget)

        return layout

    def capture_image(self, instance):
        # Capture the current frame from the camera and save it to a file
        filename = "captured_image.png"
        self.camera.export_to_png(filename)
        print(f"Image captured and saved as {filename}")

    def view_image(self, instance):
        # Display the captured image in the Image widget
        filename = "captured_image.png"
        self.image_widget.source = filename
        print(f"Viewing captured image: {filename}")

if __name__ == '__main__':
    ImageCaptureApp().run()
