from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemableBehavior


class calling_functions(MDScreen):
    def __init__(self, *args, **kwargs):
        super(calling_functions, self).__init__(**kwargs)

    def scr_new_task(self):
        if self.ids.screen_manager.current == "homescreen":
            self.ids.screen_manager.current = "new_task"  
        else:
            self.ids.screen_manager.current = "homescreen"

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"
    
        return calling_functions()
    
    
           

        

MainApp().run()