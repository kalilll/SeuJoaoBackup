from kivymd.app import MDApp
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