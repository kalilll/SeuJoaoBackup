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
    
    MDIconButton:
        icon: "menu"
        style: "tonal"
        theme_font_size: "Custom"
        theme_bg_color: "Custom"
        theme_text_color: "Custom"
        theme_icon_size: "Custom"
        text_color: "gray"
        size_hint: None, None
        pos_hint: {"center_x": .1, "center_y": .95}

    Image:
        source: "E:\\SeuJoao\\Sj\\Frame\\Tp\\Logo.png"
        size_hint_x: None
        width: dp(48)  
        pos_hint: {"center_x": .5, "center_y": .94}

    MDIconButton:
        icon: "account-circle-outline"
        style: "tonal"
        theme_font_size: "Custom"
        theme_bg_color: "Custom"
        theme_text_color: "Custom"
        theme_icon_size: "Custom"
        text_color: "gray"
        size_hint: None, None
        pos_hint: {"center_x": .9, "center_y": .95}
        
    Image:
        source: "E:\\SeuJoao\\Sj\\Frame\\Tp\\Sjf.png"
        size_hint: None, None
        size: "300dp", "300dp"
        pos_hint: {"center_x": .5, "center_y": .66}

    MDLabel:
        id: label_text
        text: "Olá! Em que posso te ajudar ?"
        theme_text_color: "Custom"
        theme_font_size: "Custom"
        size_hint: None, None 
        font_size: "19sp"
        size: "300dp", "300dp"
        pos_hint: {"center_x": .5, "center_y": 0.32}
        halign: "center"
        valign: "center"


    MDIconButton:
        id: mic_button
        icon: "microphone"
        style: "tonal"
        theme_font_size: "Custom"
        theme_bg_color: "Custom"
        theme_text_color: "Custom"
        theme_icon_size: "Custom"
        md_bg_color: "white"
        text_color: 185/255, 198/255, 217/255, 100
        font_size: "48sp"
        radius: [self.height / 2, ]
        size_hint: None, None
        size: "84dp", "84dp"
        pos_hint: {"center_x": 0.5, "center_y": .17}
        on_press: app.start()
        

"""

class SeuJoão(MDApp):
    Window.size = (300, 600)

    def build(self):
        return Builder.load_string(KV)
    
    def start(self):
        self.change_label_text()
        threading.Thread(target=self.executar_comandos_voz).start()

    def change_label_text(self):
        label_text = self.root.ids.label_text
        mic_button = self.root.ids.mic_button

        if label_text.text == "Olá! Em que posso te ajudar ?":
            label_text.text = "Ouvindo!"
            mic_button.icon = "dots-horizontal"
            
        else:
            label_text.text = "Olá! Em que posso te ajudar ?"
            mic_button.icon = "microphone"



    def falar(self, texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
        self.change_label_text()


    def ouvir(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ouvindo...")
            audio = r.listen(source)

        try:
            print("Reconhecendo...")
            query = r.recognize_google(audio, language="pt-BR")
            print(f"Usuário disse: {query}")
            return query
        except sr.UnknownValueError:
            print("Desculpe, não entendi.")
        except sr.RequestError as e:
            print(f"Desculpe, ocorreu um erro no serviço de reconhecimento de fala: {e}")

        return ""

    def executar_comandos_voz(self):
        
        while True:
            comando = self.ouvir().lower()

            if "tomada" in comando:
                self.falar("Ok! aqui está!")
                subprocess.run(["python", "E:\\SeuJoao\\Sj\\Ttom.py"])
                break
                
            elif "torneira" in comando:
                self.falar("Ok! aqui está!")
                subprocess.run(["python", "E:\\SeuJoao\\Sj\\Ttor.py"])
                break

            elif "desentupir" in comando:
                self.falar("Ok! aqui está!")
                subprocess.run(["python", "E:\\SeuJoao\\Sj\\Tpia.py"]) 
                break
           
            if not comando:
                self.change_label_text()
                break

            

SeuJoão().run()