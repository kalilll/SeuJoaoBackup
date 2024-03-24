from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel  
from kivymd.uix.button import MDIconButton
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
import pyttsx3
import speech_recognition as sr
import threading
import subprocess

KV = """
MDScreen:
    md_bg_color: 185/255, 198/255, 217/255, 100
    


    MDFloatLayout:
        size_hint: None, None  
        size: "300dp", "420dp" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.6} 
        radius: [25, 25, 25, 25]
        md_bg_color: "white"

            
        MDLabel:
            id: label_text
            text: "[b]DESENTUPIR PIA[/b]"
            markup: True
            theme_text_color: "Custom"
            theme_font_size: "Custom"
            size_hint: None, None 
            font_size: "16sp"
            size: "300dp", "50dp"  
            pos_hint: {"center_x": .5, "top": 1} 
            halign: "center"
            valign: "center"
            
        MDIcon:
            icon: "list-box"
            pos_hint: {'center_x': .05, 'center_y': 0.895}
        
        MDLabel:
            text: "[b]Materiais Necessários:[/b]"
            markup: True
            font_style: "Title" 
            role: "medium"
            pos_hint: {'center_x': .6, 'center_y': 0.89}

            MDLabel:
                text: "[font=RobotoIcons]•[/font] Um balde ou recipiente para coletar a água\n" \
                    "[font=RobotoIcons]•[/font] Luvas de proteção\n" \
                    "[font=RobotoIcons]•[/font] Uma chave inglesa"
                markup: True
                font_size: "14sp"
               


        

            
                


 
            

    MDIconButton:
        id: back_button
        icon: "arrow-left"
        style: "standard"
        theme_font_size: "Custom"
        theme_bg_color: "Custom"
        theme_text_color: "Custom"
        theme_icon_size: "Custom"
        text_color: "black"
        font_size: "48sp"
        radius: [self.height / 2, ]
        size_hint: None, None
        size: "44dp", "44dp"
        pos_hint: {"center_x": 0.17, "center_y": .17}
        on_press: app.switch_to_second_app()


    MDIconButton:
        id: 3d_button
        icon: "video-3d"
        style: "standard"
        theme_font_size: "Custom"
        theme_bg_color: "Custom"
        theme_text_color: "Custom"
        theme_icon_size: "Custom"
        text_color: "black"
        font_size: "48sp"
        radius: [self.height / 2, ]
        size_hint: None, None
        size: "44dp", "44dp"
        pos_hint: {"center_x": .83, "center_y": .17}


"""


class SeuJoão(MDApp):
    Window.size = (300, 600)

    def build(self):
        return Builder.load_string(KV)
    
    def switch_to_second_app(self):
        subprocess.run(["python", "E:\\SeuJoao\\Sj\\Tp.py"])
 
    
SeuJoão().run()