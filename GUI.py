import kivy
from kivy.app import App
from kivy.uix.label import Label

#The Base class of our App should always inherit from
#the App class.

class GebApp(App):
    def build(self):
        #This is where we should initialize and
        #return the root widget:
        return Label(text='Hello world')



if __name__=="__main__":
    GebApp().run()
