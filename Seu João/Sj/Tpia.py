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
        Clock.schedule_once(lambda dt: self.update_result_screen("DESENTUPIR PIA", center=True, add_space=True, space_height= -20), 1)
        Clock.schedule_once(lambda dt: self.update_result_screen("Reúna os Materiais Necessários:", bold=True, add_space=True, space_height= -20), 2)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Balde ou Recipiente",add_space=True, space_height=-20), 3)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Chave Inglesa", add_space=True, space_height=-20), 4)
        Clock.schedule_once(lambda dt: self.update_result_screen("Feche o Registro de Água:", bold=True, add_space=True, space_height=35), 5)
        Clock.schedule_once(lambda dt: self.update_result_screen("Certifique-se de fechar o registro de água para evitar vazamentos ou acidentes durante o processo.", add_space=True, space_height=15), 6)
        Clock.schedule_once(lambda dt: self.update_result_screen("Posicione o Balde:", bold=True, add_space=True, space_height=35), 7)
        Clock.schedule_once(lambda dt: self.update_result_screen("Coloque um balde ou recipiente grande embaixo do sifão para coletar a água que pode escorrer.", add_space=True, space_height=15), 8)
        Clock.schedule_once(lambda dt: self.update_result_screen("Desparafuse o Sifão:", bold=True, add_space=True, space_height=65), 9)
        Clock.schedule_once(lambda dt: self.update_result_screen("Use uma chave inglesa para afrouxar as porcas que prendem o sifão. Tenha cuidado ao soltar as porcas para não danificar o encanamento ou o sifão.", add_space=True, space_height=50), 10)
        Clock.schedule_once(lambda dt: self.update_result_screen("Desconecte o Sifão:", bold=True, add_space=True, space_height=50), 11)
        Clock.schedule_once(lambda dt: self.update_result_screen("Retire o sifão com cuidado para evitar derramamento de água e detritos. Coloque o sifão no balde para esvaziá-lo e limpá-lo.", add_space=True, space_height=35), 12)
        Clock.schedule_once(lambda dt: self.update_result_screen("Limpe o Sifão:", bold=True, add_space=True, space_height=80), 13)
        Clock.schedule_once(lambda dt: self.update_result_screen("Use uma escova para limpar os detritos, cabelos ou resíduos que possam estar obstruindo o sifão. Certifique-se de remover completamente quaisquer bloqueios ou acúmulos.", add_space=True, space_height= 65), 14)
        Clock.schedule_once(lambda dt: self.update_result_screen("Verifique a Tubulação Adjacente:", bold=True, add_space=True, space_height=80), 15)
        Clock.schedule_once(lambda dt: self.update_result_screen("Enquanto o sifão estiver removido, verifique se há obstruções ou detritos na tubulação adjacente. Se encontrar alguma obstrução, limpe-a cuidadosamente com a escova ou com água corrente.", add_space=True, space_height= 65), 16)
        Clock.schedule_once(lambda dt: self.update_result_screen("Conecte o Sifão:", bold=True, add_space=True, space_height=50), 17)
        Clock.schedule_once(lambda dt: self.update_result_screen("Certifique-se de apertar as porcas do sifão com a chave inglesa para garantir uma conexão segura e sem vazamentos.", add_space=True, space_height=35), 18)
        Clock.schedule_once(lambda dt: self.update_result_screen("Teste a Pia:", bold=True, add_space=True, space_height=35), 19)
        Clock.schedule_once(lambda dt: self.update_result_screen("Abra o registro de água e teste a pia para garantir que a água flua sem problemas.", add_space=True, space_height=160), 21)
        Clock.schedule_once(lambda dt: self.update_result_screen("Se o problema persistir mesmo após limpar o sifão, pode haver um problema mais complexo no sistema de encanamento. Nesse caso, pode ser necessário chamar um encanador profissional para avaliar a situação e fornecer uma solução adequada.", bold=True, add_space=True, space_height=100), 22)

SeuJoão().run()
