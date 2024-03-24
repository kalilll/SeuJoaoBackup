from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel  
from kivymd.uix.button import MDIconButton
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import subprocess

KV = """
MDScreen:
    md_bg_color: 185/255, 198/255, 217/255, 100

    ScrollView:
        id: scroll_view
        size_hint: None, None
        size: "300dp", "470dp" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.55} 

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            spacing: "5dp"
            height: self.minimum_height
            md_bg_color: "white"
            radius: [25, 25, 25, 25]

            MDFloatLayout: 
                id: float_layout
                size_hint: None, None
                orientation: 'vertical' 
                size: "300dp", "700dp"
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
                    size: "300dp", "30dp"  
                    pos_hint: {"center_x": .5, "top": 1} 
                    halign: "center"
                    valign: "center"
                

                MDLabel:
                    text: "[b]Materiais Necessários:[/b]"
                    markup: True
                    theme_text_color: "Custom"
                    theme_font_size: "Custom"
                    size_hint: None, None 
                    size: "300dp", "30dp" 
                    font_style: "Title" 
                    role: "medium"
                    pos_hint: {'center_x': .55, 'center_y': .94}    

            MDLabel
            

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
        pos_hint: {"center_x": 0.17, "center_y": .1}
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
        pos_hint: {"center_x": .83, "center_y": .1}
"""

class SeuJoão(MDApp):
    Window.size = (300, 600)

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_once(self.scroll_to_end, 0.1)


    def scroll_to_end(self, dt):
        scroll_view = self.root.ids.scroll_view
        scroll_view.scroll_y = 1.0


    def switch_to_second_app(self):
        subprocess.run(["python", "E:\\SeuJoao\\Sj\\Tp.py"])

SeuJoão().run()
