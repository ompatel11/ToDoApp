from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

class Cards(MDCard):
    
    def create_cards(self):
        pass
class calling_functions(MDScreen):
    def __init__(self, *args, **kwargs):
        super(calling_functions, self).__init__(**kwargs)
        self.no_files = 5
        self.lists_fl = []
        for i in range(self.no_files):
            k = Cards(id=f"{i}")
            self.lists_fl.append(k)
        self.lists_fl[0].pos_hint = {'bottom':1}
        for j in range(5):
            
            self.lists_fl[j].add_widget(MDLabel(text="Hi World"))
            self.ids.md_list.add_widget(self.lists_fl[j])
             
    def change_screen(self):
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