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
        Clock.schedule_once(lambda dt: self.update_result_screen("TRATAR FISSURA", center=True, add_space=True, space_height= -20),1)
        Clock.schedule_once(lambda dt: self.update_result_screen("Reúna os Materiais Necessários:", bold=True, add_space=True, space_height= -20),2)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Escova de Arame", add_space=True, space_height=-20),3)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Espátula de Aço", add_space=True, space_height=-20),4)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Lixa de Parede", add_space=True, space_height=-20),5)
        Clock.schedule_once(lambda dt: self.update_result_screen("Massa Corrida ou Selante", add_space=True, space_height=-20),6)
        Clock.schedule_once(lambda dt: self.update_result_screen("Tinta (opcional)", add_space=True, space_height=-20),7)
        Clock.schedule_once(lambda dt: self.update_result_screen("ATENÇÃO:", bold=True, add_space=True, space_height=230),8)
        Clock.schedule_once(lambda dt: self.update_result_screen("Examine a fissura para determinar sua causa e extensão. Fissuras podem ocorrer devido a assentamento natural da casa, mudanças de temperatura, umidade, movimento do solo, entre outros motivos. Se a fissura for muito extensa ou se houver preocupações sobre a integridade estrutural da parede, pode ser prudente consultar um profissional, como um empreiteiro ou engenheiro civil, para avaliar a situação e recomendar soluções adequadas.", add_space=True, space_height=210),9)
        Clock.schedule_once(lambda dt: self.update_result_screen("Limpeza da Área:", bold=True, add_space=True, space_height=65),10)
        Clock.schedule_once(lambda dt: self.update_result_screen("Remova qualquer sujeira, poeira ou detritos da fissura para garantir que qualquer material de preenchimento que você aplicar adere adequadamente.", add_space=True, space_height=45),11)
        Clock.schedule_once(lambda dt: self.update_result_screen("Preparação da Superfície:", bold=True, add_space=True, space_height=65),12)
        Clock.schedule_once(lambda dt: self.update_result_screen("Use uma escova de arame ou um raspador para alargar ligeiramente a fissura e remover quaisquer partes soltas ou descascadas de tinta ou gesso ao redor dela.", add_space=True, space_height=65),13)
        Clock.schedule_once(lambda dt: self.update_result_screen("Aplicação da Massa Corrida ou Selante:", bold=True, add_space=True, space_height=130),14)
        Clock.schedule_once(lambda dt: self.update_result_screen("Preencha a fissura com massa corrida (também conhecida como massa para drywall) ou um selante próprio para fissuras em paredes. Use uma espátula para aplicar o material de forma uniforme, pressionando-o bem na fissura.", add_space=True, space_height=95),15)
        Clock.schedule_once(lambda dt: self.update_result_screen("Suavização da superfície:", bold=True, add_space=True, space_height=65),16)
        Clock.schedule_once(lambda dt: self.update_result_screen("Depois que o material de preenchimento estiver seco, use uma lixa fina para suavizar a superfície e nivelar qualquer irregularidade.", add_space=True, space_height= 45),17)
        Clock.schedule_once(lambda dt: self.update_result_screen("Pintura:", bold=True, add_space=True, space_height=65),18)
        Clock.schedule_once(lambda dt: self.update_result_screen("Se necessário, pinte a área preparada para combinar com o resto da parede. Certifique-se de que a tinta aplicada se misture bem com a cor existente.", add_space=True, space_height= 45),19)
        Clock.schedule_once(lambda dt: self.update_result_screen("Monitoramento contínuo:", bold=True, add_space=True, space_height=110),20)
        Clock.schedule_once(lambda dt: self.update_result_screen("Após o reparo, monitore a fissura periodicamente para garantir que não haja reaparecimento ou alargamento. Se a fissura reaparecer ou se expandir, pode ser necessário investigar problemas estruturais mais graves.", add_space=True, space_height=60),21)

SeuJoão().run()
