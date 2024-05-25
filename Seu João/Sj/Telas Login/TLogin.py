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
    md_bg_color: "white"


    MDLabel:
        text: "         B e m   V i n d o (a) !"
        theme_text_color: "Custom"
        theme_font_size: "Custom"
        theme_font_name: "Custom"
        size_hint: None, None 
        font_size: "20sp"
        text_color: "4477CE"
        bold: "True"
        size: "300dp", "300dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        font_name: "Sj\Fonts\Poppins-ExtraBold.ttf"
        halign: "left"
        valign: "center"


    MDLabel:
        text: "           Faça login para continuar!"
        theme_text_color: "Custom"
        theme_font_size: "Custom"
        size_hint: None, None 
        text_color: "gray"
        font_size: "15sp"
        size: "300dp", "300dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.85} 
        halign: "left"
        valign: "center"



  
         
    




    MDBoxLayout:

        md_bg_color: "white"
        orientation: "vertical"
        spacing: "20dp"
        adaptive_height: True
        size_hint_x: .8
        pos_hint: {"center_x": .5, "center_y": .6}


        MDTextField:
            mode: "filled"
            adaptive_height: True
            size_hint: None, None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .9}
            theme_line_color: "Custom"
            line_color_focus: "gray"
            line_color_normal: "gray"
            theme_bg_color: "Custom"
            fill_color_normal: "white"
            fill_color_focus: "white"



            MDTextFieldHintText:
                text: "Email"
                theme_text: "Custom"
                text_color_focus: "gray"
                text_color_normal: "gray"
                

            MDTextFieldHelperText:
                text: "user@gmail.com"
                mode: "on_focus"
                text_color: "gray"

        
                



        MDTextField:
            mode: "filled"
            adaptive_height: True
            size_hint: None, None
            width: "240dp"
            pos_hint: {"center_x": .5, "center_y": .9}
            theme_line_color: "Custom"
            line_color_focus: "gray"
            line_color_normal: "gray"
            theme_bg_color: "Custom"
            fill_color_normal: "white"
            fill_color_focus: "white"

            
            MDTextFieldHintText:
                text: "Senha"
                theme_text: "Custom"
                text_color_focus: "gray"
                text_color_normal: "gray"

                
            MDTextFieldHelperText:
                text: "*Sua senha deve ter no mínimo 8 caracteres"
                mode: "on_focus"
                text_color: "red"
            
                
    MDButton:
        style: "filled"
        theme_bg_color: "Custom"
        md_bg_color: "4477CE"
        radius: [10]
        pos_hint: {"center_x": .5, "center_y": .4}
        halign: "center"

        MDButtonText:
            text: "LOGIN"
            theme_text_color: "Custom"
            text_color: "white"

    
    MDButton:
        style: "text"
        radius: [10]
        pos_hint: {"center_x": .5, "center_y": .33}
        halign: "center" 

        MDButtonText:
            text: "Esqueçeu sua senha?"
            theme_text_color: "Custom"
            text_color: "4477CE"

    MDBoxLayout:
        md_bg_color: "white"
        orientation: "vertical"
        adaptive_height: True 
        size: "300dp", "1dp" 
        pos_hint: {"center_x": .5, "center_y": .29}

        MDFloatLayout:
            md_bg_color: "gray"
            size_hint: .3,  .002 
            pos_hint:{"center_x": .3, "center_y": 0.3}


        MDFloatLayout:
            md_bg_color: "gray"
            size_hint: .3,  .002 
            pos_hint:{"center_x": .7, "center_y": 0.3}

            

  

    MDButton:
        style: "text"
        radius: [10]
        size_hint: None, None
        pos_hint: {"center_x": .75, "center_y": 0.05}
        halign: "center" 
        valign: "center"

        MDButtonText:
            text: "Sing Up"
            theme_text_color: "Custom"
            text_color: "4477CE"
            

            


                
                




            


    




"""

class SeuJoão(MDApp):
    Window.size = (300, 600)

    def build(self):
        return Builder.load_string(KV)
    
SeuJoão().run()