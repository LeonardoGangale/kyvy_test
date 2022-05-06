from itertools import count
from tkinter.tix import Tree
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.core.window import Window 

from kivy.lang import Builder
from kivymd.app import MDapp

class CanvasExample2(Widget):
    Window.borderless = True

class WidgetsExample(GridLayout):
    my_text = StringProperty("0")
    count = 0
    enabled = BooleanProperty(False)
    slider_value_text  = StringProperty("50")
    input_text = StringProperty("inserisci qui il testo")
    def click_del_bottone(self):
        if self.enabled:
            print("il bottone funziona!")
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_state(self, toggle_button):
        print("toggle state: " + toggle_button.state)
        if toggle_button.state == "normal":
            toggle_button.text = "off"
            self.enabled = False
        elif toggle_button.state == "down":
            toggle_button.text = "on"   # il widget esiste già quindi possiamo cambiare il testo direttamente così
            self.enabled = True
    
    def on_switch_active(self, switch):
        print("switch: " + str(switch.active))

    def on_enter_key(self, text_input):
        self.input_text = text_input.text



























class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # per impostare l'orientamento:
        # self.orientation = ""
        for i in range (100):
            b = Button(text=str(i+1), size_hint=(None,None), size=(dp(100), dp(100)))
            self.add_widget(b)

"""
class BoxLayoutExample(BoxLayout):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation  = "vertical"      # cambia l'orientamento del boxlayout
        b1 = Button(text="ciao A")
        b2 = Button(text="ciao B")
        b3 = Button(text="ciao C")
        self.add_widget(b1)     # cambia l'orientamento del boxlayout
        self.add_widget(b2)
        self.add_widget(b3)
    """

class MainWidget(Widget):
    pass

class primoApp(App):
    pass

primoApp().run()