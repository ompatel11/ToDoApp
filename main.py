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
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList
from kivy.uix.scatter import Scatter
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase



class Dynamic_card(MDFloatLayout):
    id = StringProperty()
    

    def delete_task(self):
        print(obj)
        print(main_obj.ids.sl_home.ids)
        # main_obj.ids.sl_home.remove_widget(obj)        
        main_obj.ids.sl_home.remove_widget(obj)

class calling_functions(MDScreen):
    obj_id  = 0 
    global list_obj 
    list_obj = []
    def __init__(self, *args, **kwargs):
        super(calling_functions, self).__init__(**kwargs)
        self.no_files = 0
        obj = []
        for i in range(self.no_files):
            obj.append(Dynamic_card()) 
            self.ids.sl_home.add_widget(obj[i])
        for o in obj:
            j = 0 
            o.id = f"{j}"   
            print(o.id)
            j = j + 1   
    
    def change_screen(self):
        """Change the display screen """
        if self.ids.screen_manager.current == "homescreen":
            self.ids.screen_manager.current = "new_task"  
        elif self.ids.screen_manager.current == "new_task":
            self.ids.screen_manager.current = "homescreen"
                
    def generate_id(self):
        self.obj_id = self.obj_id + 1
        return(self.obj_id)

    def create_task(self):
        """Create object of Dynamic_card class and add it to the Main window """ 
        
        self.ids.screen_manager.current = "homescreen"
        id_of_obj = "obj_"+ str(self.generate_id())
        global obj 
        obj = Dynamic_card()
        obj.id = str(id_of_obj)
        obj.size_hint = [.5,None]
        if self.ids.txt_create_body.height <= 100:
            obj.size_hint = [.5,.1]
        elif self.ids.txt_create_body.height >=400:
            obj.size_hint = [.5,.5]
        else:
            obj.height = self.ids.txt_create_body.height
        obj.ids.lbl_title.text = self.ids.txt_create_title.text
        obj.ids.lbl_body.text = self.ids.txt_create_body.text
        list_obj.append(obj)
        print(obj.id)
        for i in list_obj:
            i.id=str(id_of_obj)
        self.ids.sl_home.add_widget(obj)
        self.ids.txt_create_body.text = " "
        self.ids.txt_create_title.text = " "


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        global main_obj
        main_obj = calling_functions()
        return main_obj
    
    
           

        

MainApp().run()