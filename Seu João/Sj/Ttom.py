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
        Clock.schedule_once(lambda dt: self.update_result_screen("TROCAR DE TOMADA", center=True, add_space=True, space_height= -20),1)
        Clock.schedule_once(lambda dt: self.update_result_screen("Reúna os materiais necessários:", bold=True, add_space=True, space_height= -20),2)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Chave de Fenda", add_space=True, space_height=-20),3)
        Clock.schedule_once(lambda dt: self.update_result_screen("1 Alicate de Corte", add_space=True, space_height=-20),4)
        Clock.schedule_once(lambda dt: self.update_result_screen("Desligue a energia elétrica:", bold=True, add_space=True, space_height=80),5)
        Clock.schedule_once(lambda dt: self.update_result_screen("Certifique-se de desligar a energia elétrica na área onde você vai trabalhar. Isso pode ser feito desligando o disjuntor correspondente no quadro de distribuição de energia.", add_space=True, space_height=65),6)
        Clock.schedule_once(lambda dt: self.update_result_screen("Remova a tomada antiga:", bold=True, add_space=True, space_height=180),7)
        Clock.schedule_once(lambda dt: self.update_result_screen("Use uma chave de fenda para soltar os parafusos que prendem a tampa da tomada à caixa elétrica. Em seguida, retire a tampa e use um alicate para soltar os parafusos que prendem os fios à tomada antiga. Lembre-se de anotar qual fio estava conectado a cada terminal (geralmente um fio preto ou vermelho no terminal [Fase] e um fio azul ou branco no terminal [Neutro].", add_space=True, space_height=160),8)
        Clock.schedule_once(lambda dt: self.update_result_screen("Prepare a nova tomada:", bold=True, add_space=True, space_height=65),9)
        Clock.schedule_once(lambda dt: self.update_result_screen("Prepare a nova tomada, retirando a tampa da mesma forma que fez com a antiga. Certifique-se de que os fios estejam devidamente descascados nas pontas.", add_space=True, space_height=45),10)
        Clock.schedule_once(lambda dt: self.update_result_screen("Conecte os fios:", bold=True, add_space=True, space_height=145),11)
        Clock.schedule_once(lambda dt: self.update_result_screen("Conecte os fios da nova tomada aos terminais correspondentes. O fio de fase deve ser conectado ao terminal -Fase- (geralmente marcado com [L] ou [+]), e o fio neutro deve ser conectado ao terminal [Neutro] (geralmente marcado com [N] ou [-]). Aperte bem os parafusos para garantir uma conexão segura.", add_space=True, space_height=130),12)
        Clock.schedule_once(lambda dt: self.update_result_screen("Fixe a nova tomada:", bold=True, add_space=True, space_height=65),13)
        Clock.schedule_once(lambda dt: self.update_result_screen("Posicione a nova tomada na caixa elétrica e prenda-a usando os parafusos que vieram com a tomada. Certifique-se de que a tomada esteja bem fixa e nivelada.", add_space=True, space_height= 50),14)
        Clock.schedule_once(lambda dt: self.update_result_screen("Coloque a tampa:", bold=True, add_space=True, space_height=30),15)
        Clock.schedule_once(lambda dt: self.update_result_screen("Encaixe a tampa na nova tomada e aperte os parafusos para prendê-la na posição.", add_space=True, space_height= 20),16)
        Clock.schedule_once(lambda dt: self.update_result_screen("Ligue a energia elétrica:", bold=True, add_space=True, space_height=50),17)
        Clock.schedule_once(lambda dt: self.update_result_screen("Volte ao quadro de distribuição de energia e ligue o disjuntor correspondente à tomada que você acabou de trocar.", add_space=True, space_height=30),18)
        Clock.schedule_once(lambda dt: self.update_result_screen("Verifique o funcionamento:", bold=True, add_space=True, space_height=30),19)
        Clock.schedule_once(lambda dt: self.update_result_screen("Plugue um dispositivo na nova tomada e verifique se ele funciona corretamente.", add_space=True, space_height=125),20)


SeuJoão().run()
 