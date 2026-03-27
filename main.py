from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.95, 0.95, 0.95, 1)

class IMCIApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40)
        layout.add_widget(Label(text="نظام IMCI - اليمن", font_size='24sp', color=(0, 0.4, 0.2, 1), bold=True))
        layout.add_widget(Label(text="جاري معالجة البيانات...", color=(0.2, 0.2, 0.2, 1)))
        return layout

if __name__ == "__main__":
    IMCIApp().run()
