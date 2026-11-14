from kivy.app import App
from kivy.uix.button import Button

class PrankApp(App):
    def build(self):
        return Button(text='System Guard Pro\nВнимание: Угроза обнаружена!', font_size=24)

if __name__ == '__main__':
    PrankApp().run()
