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
        Clock.schedule_once(lambda dt: self.update_result_screen("TROCAR DE TORNEIRA", center=True, add_space=True, space_height=-20),1)
        Clock.schedule_once(lambda dt: self.update_result_screen("Reúna os materiais necessários:", bold=True, add_space=True, space_height=-20),2)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Chave Inglesa", add_space=True, space_height=-20),3)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Chave de Grifo", add_space=True, space_height=-20),4)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Fita Veda Rosca", add_space=True, space_height=-20),5)
        Clock.schedule_once(lambda dt: self.update_result_screen("Desligue a água:", bold=True, add_space=True, space_height=50),6)
        Clock.schedule_once(lambda dt: self.update_result_screen("Antes de fazer qualquer alteração na torneira, certifique-se de fechar o registro de água principal para evitar vazamentos ou danos.", add_space=True, space_height=30),7)
        Clock.schedule_once(lambda dt: self.update_result_screen("Remova a torneira antiga:", bold=True, add_space=True, space_height=85),8)
        Clock.schedule_once(lambda dt: self.update_result_screen("Use uma chave inglesa ou uma chave de grifo para soltar as porcas de fixação que prendem a torneira ao lavatório ou pia. Em seguida, desenrosque a torneira antiga e remova-a completamente.", add_space=True, space_height=65),9)
        Clock.schedule_once(lambda dt: self.update_result_screen("Limpe a área de instalação:", bold=True, add_space=True, space_height=65),10)
        Clock.schedule_once(lambda dt: self.update_result_screen("Limpe a área onde a torneira estava instalada para remover quaisquer resíduos ou depósitos que possam interferir na instalação da nova torneira.", add_space=True, space_height=45),11)
        Clock.schedule_once(lambda dt: self.update_result_screen("Instale a nova torneira:", bold=True, add_space=True, space_height=100),12)
        Clock.schedule_once(lambda dt: self.update_result_screen("Insira a nova torneira no furo da pia ou do lavatório e aperte as porcas de fixação usando a chave inglesa. Certifique-se de que a torneira esteja alinhada corretamente e que esteja firme e nivelada.", add_space=True, space_height=80),13)
        Clock.schedule_once(lambda dt: self.update_result_screen("Conecte os canos:", bold=True, add_space=True, space_height=80),14)
        Clock.schedule_once(lambda dt: self.update_result_screen("Conecte os canos da torneira às tubulações de água. Use a fita de encanador para garantir uma vedação hermética. Certifique-se de que todas as conexões estejam apertadas.", add_space=True, space_height= 65),15)
        Clock.schedule_once(lambda dt: self.update_result_screen("Teste a torneira:", bold=True, add_space=True, space_height=85),16)
        Clock.schedule_once(lambda dt: self.update_result_screen("Ligue o fornecimento de água e teste a nova torneira para garantir que não haja vazamentos. Verifique se há vazamentos nas conexões e se a água flui corretamente.", add_space=True, space_height= 65),17)
        Clock.schedule_once(lambda dt: self.update_result_screen("Faça ajustes finais:", bold=True, add_space=True, space_height=50),18)
        Clock.schedule_once(lambda dt: self.update_result_screen("Faça os ajustes necessários para garantir que a torneira esteja funcionando corretamente e que não haja vazamentos.", add_space=True, space_height=190),19)
        Clock.schedule_once(lambda dt: self.update_result_screen("Seguindo esses passos, você deve ser capaz de trocar uma torneira com relativa facilidade. No entanto, se você se sentir desconfortável em lidar com o trabalho de encanamento, é sempre recomendável contratar um profissional para fazer o serviço.", bold=True, add_space=True, space_height=125),20)

SeuJoão().run()
