import time
from kivy.app import App
from kivy.clock import Clock
from kivymd.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (400, 700)

class myclock(Label):
    def update(self, *args):
        self.text = time.asctime()
class TimeApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        
        clock1 = myclock()
        
        Clock.schedule_interval(clock1.update, .1)
        layout.add_widget(clock1) 
        
        layout.add_widget(Label(text='Italy'))       
        return layout

if __name__ == '__main__':
    TimeApp().run()
    
