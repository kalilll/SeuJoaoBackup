from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDLabel:
        text: "Clique [ref=example]aqui[/ref] para visitar o Google."
        markup: True
        on_ref_press: app.open_link("https://www.google.com")
'''


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def open_link(self, link):
        import webbrowser
        webbrowser.open(link)


TestApp().run()
