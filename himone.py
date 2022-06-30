from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader

class Greetings(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint= (0.6,0.7)
        self.window.pos_hint = {"center_x" : 0.5, "center_y" :0.5}
        #add widgets to window

        #image widget

        self.window.add_widget(Image(source="Shape-2.png"))
       
        #Label widget
        self.greeting = Label(text="What's your name?",
                              font_size = 18,
                              color="860556"
                              )
        self.window.add_widget(self.greeting)

        #text input widget
        self.user = TextInput(multiline=False,
                              padding_y = (20,20),
                              size_hint = (1,0.5)
                              )
        self.window.add_widget(self.user)

        #button widget
        self.button = Button(text="PRESS KARO",
                             size_hint = (1,0.5),
                             bold = True,
                             background_color = "860556" 
                             )
        self.window.add_widget(self.button)
        self.button.bind(on_press=self.callback)
        self.button.bind(on_press=self.play_sound)
   

        return self.window
    
    def callback(self, instance):
        self.greeting.text = "NEE POI CHAAV"
    def play_sound(self, instance):
        sound = SoundLoader.load("sugamalle.mp3")
        if sound:
            sound.play()


if __name__ == "__main__":
    Greetings().run()
