from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
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

    Image:
        source: "E:\\SeuJoao\\Sj\\Frame\\Tp\\Logo.png"
        size_hint_x: None
        width: dp(48)  
        pos_hint: {"center_x": .5, "center_y": .94}
    
    MDBoxLayout:
        orientation: "vertical"
        spacing: "40dp"
        adaptive_height: True
        size_hint_x: .8
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            mode: "filled"
            size_hint_x: None
            adaptive_height: True
            size_hint: None, None
            width: "240dp"
            pos_hint: {"center_x": .5}
            theme_line_color: "Custom"
            line_color_focus: "black"
            theme_bg_color: "Custom"
            fill_color_normal: 185/255, 198/255, 217/255, 100
            fill_color_focus: 185/255, 198/255, 217/255, 100
            


            MDTextFieldLeadingIcon:
                icon: "account"

            MDTextFieldHintText:
                text: "Nome"
                text_color_focus: "black"
                theme_text: "Custom"
                text_color_focus: "black"               


            MDTextFieldHelperText:
                text: "Insira seu primeiro nome!"
                mode: "persistent"

        MDTextField:
            mode: "filled"
            adaptive_height: True
            size_hint: None, None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .9}
            theme_line_color: "Custom"
            line_color_focus: "black"
            theme_bg_color: "Custom"
            fill_color_normal: 185/255, 198/255, 217/255, 100
            fill_color_focus: 185/255, 198/255, 217/255, 100
                        


            MDTextFieldLeadingIcon:
                icon: "email"

            MDTextFieldHintText:
                text: "Email"
                theme_text: "Custom"
                text_color_focus: "black"


            MDTextFieldHelperText:
                text: "user@gmail.com"
                mode: "persistent"
        
        MDTextField:
            mode: "filled"
            adaptive_height: True
            size_hint: None, None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .9}
            theme_line_color: "Custom"
            line_color_focus: "black"
            theme_bg_color: "Custom"
            fill_color_normal: 185/255, 198/255, 217/255, 100
            fill_color_focus: 185/255, 198/255, 217/255, 100
            


            MDTextFieldLeadingIcon:
                icon: "lock"

            MDTextFieldHintText:
                text: "Senha"
                theme_text: "Custom"
                text_color_focus: "black"

            MDTextFieldHelperText:
                text: "*Sua senha deve ter no mínimo 8 caracteres"
                mode: "persistent"
                text_color: "red"




            


    




"""

class SeuJoão(MDApp):
    Window.size = (300, 600)

    def build(self):
        return Builder.load_string(KV)
    
SeuJoão().run()