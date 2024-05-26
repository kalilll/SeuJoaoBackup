from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel  
from kivymd.uix.button import MDIconButton
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import subprocess

KV = """
MDScreen:
    md_bg_color: 185/255, 198/255, 217/255, 100
    
    MDBoxLayout:
        md_bg_color: "white"
        orientation: "vertical"
        padding: "5dp"
        pos_hint: {"center_x": .5, "center_y": .53}
        halign: "center"
        valign: "center"
        size_hint: None, None
        size: "300dp", "400dp"
        radius: [10]
        MDScrollView:
            id: scroll
            MDBoxLayout:
                id: box
                orientation: "vertical"
                spacing: "25dp"
                adaptive_height: True
                size_hint_x: 1
                size_hint_y: None  # Change to None for adaptive height
                pos_hint: {"center_x": .5, "center_y": .6}
                
                MDLabel:
                          
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
    label_text = ObjectProperty()

    def build(self):
        self.root = Builder.load_string(KV)
        self.text_box = self.root.ids.box  # Reference to the MDBoxLayout inside the scrollview
        self.scroll_view = self.root.ids.scroll  # Reference to the ScrollView
        return self.root

    def switch_to_second_app(self):
        subprocess.run(["python", "E:\\SeuJoao\\Sj\\Tp.py"])

    def update_result_screen(self, text, bold=False, add_space=False, space_height=0, center=False):
        if bold:
            text = f"[b]{text}[/b]"
        new_label = MDLabel(
            text=text,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            theme_font_size="Custom",
            font_size="19sp",
            markup=True,
            halign='center' if center else 'left'
        )
        self.text_box.add_widget(new_label)

        if add_space:
            spacer = Widget(size_hint_y=None, height=space_height)
            self.text_box.add_widget(spacer)

        # Schedule to scroll to the bottom after adding the new text
        Clock.schedule_once(self.scroll_to_bottom, 0.1)

    def scroll_to_bottom(self, dt):
        self.scroll_view.scroll_y = 0

    def on_start(self):
        Clock.schedule_once(lambda dt: self.update_result_screen("TRATAR MANCHA DE MOFO", center=True, add_space=True, space_height= -20),1)
        Clock.schedule_once(lambda dt: self.update_result_screen("Reúna os Materiais Necessários:", bold=True, add_space=True, space_height= -20),2)
        Clock.schedule_once(lambda dt: self.update_result_screen("Luvas de Borracha", add_space=True, space_height=-20),3)
        Clock.schedule_once(lambda dt: self.update_result_screen("Óculos de Proteção", add_space=True, space_height=-20),4)
        Clock.schedule_once(lambda dt: self.update_result_screen("Máscara Facial", add_space=True, space_height=-20),5)
        Clock.schedule_once(lambda dt: self.update_result_screen("Água", add_space=True, space_height=-20),6)
        Clock.schedule_once(lambda dt: self.update_result_screen("Detergente Neutro", add_space=True, space_height=-20),7)
        Clock.schedule_once(lambda dt: self.update_result_screen("Esponja ou Escova", add_space=True, space_height=-20),8)
        Clock.schedule_once(lambda dt: self.update_result_screen("Água Sanitária", add_space=True, space_height=-20),9)
        Clock.schedule_once(lambda dt: self.update_result_screen("Proteção Pessoal:", bold=True, add_space=True, space_height=50),10)
        Clock.schedule_once(lambda dt: self.update_result_screen("Antes de começar, use luvas de borracha, óculos de proteção e uma máscara facial para evitar a inalação de esporos de mofo.", add_space=True, space_height=30),11)
        Clock.schedule_once(lambda dt: self.update_result_screen("Ventilação:", bold=True, add_space=True, space_height=65),12)
        Clock.schedule_once(lambda dt: self.update_result_screen("Abra as janelas para permitir a ventilação adequada no ambiente. Isso ajudará a reduzir a umidade e a dispersar os esporos de mofo durante o processo de limpeza.", add_space=True, space_height=50),13)
        Clock.schedule_once(lambda dt: self.update_result_screen("Remoção da Umidade:", bold=True, add_space=True, space_height=100),14)
        Clock.schedule_once(lambda dt: self.update_result_screen("Identifique e corrija qualquer problema de umidade na parede. Pode ser necessário consertar vazamentos de encanamento, melhorar a ventilação ou usar um desumidificador para reduzir a umidade ambiente.", add_space=True, space_height=80),15)
        Clock.schedule_once(lambda dt: self.update_result_screen("Limpeza da Mancha de Mofo:", bold=True, add_space=True, space_height=100),16)
        Clock.schedule_once(lambda dt: self.update_result_screen("Misture uma solução de água e detergente neutro em um balde. Use uma esponja ou escova macia para limpar suavemente a mancha de mofo. Evite usar muita água, pois isso pode agravar o problema de umidade.", add_space=True, space_height=80),17)
        Clock.schedule_once(lambda dt: self.update_result_screen("Desinfecção:", bold=True, add_space=True, space_height=180),18)
        Clock.schedule_once(lambda dt: self.update_result_screen("Depois de limpar a mancha de mofo, é importante desinfetar a área para matar quaisquer esporos remanescentes. Você pode usar uma solução de água sanitária diluída em água (cerca de 1 parte de água sanitária para 10 partes de água). Aplique a solução com um pano limpo e deixe agir por alguns minutos antes de enxaguar com água limpa.", add_space=True, space_height= 165),19)
        Clock.schedule_once(lambda dt: self.update_result_screen("Secagem Completa:", bold=True, add_space=True, space_height=65),20)
        Clock.schedule_once(lambda dt: self.update_result_screen("Certifique-se de que a parede esteja completamente seca após a limpeza. Use ventiladores ou desumidificadores para acelerar o processo, se necessário.", add_space=True, space_height= 50),21)
        Clock.schedule_once(lambda dt: self.update_result_screen("Prevenção de Futuros Problemas:", bold=True, add_space=True, space_height=115),22)
        Clock.schedule_once(lambda dt: self.update_result_screen("Para evitar o retorno do mofo, mantenha a área bem ventilada e livre de umidade excessiva. Considere usar uma tinta antimicrobiana ou um primer selante após a limpeza para ajudar a prevenir o crescimento futuro de mofo.", add_space=True, space_height=100),23)
        Clock.schedule_once(lambda dt: self.update_result_screen("ATENÇÃO:", bold=True, add_space=True, space_height=100),24)
        Clock.schedule_once(lambda dt: self.update_result_screen("Se a mancha de mofo for muito extensa ou se você tiver dificuldade em removê-la, pode ser necessário consultar um profissional em remoção de mofo para uma limpeza mais completa e segura.",add_space=True, space_height=100),25)
SeuJoão().run()
