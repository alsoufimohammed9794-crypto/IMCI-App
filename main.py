from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class IMCIApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        layout.add_widget(Label(text="نظام IMCI - التدبير المتكامل", font_size='24sp'))
        
        sections = ["تقييم علامات الخطر", "السعال وصعوبة التنفس", "الإسهال والجفاف", "الحمى وسوء التغذية"]
        for section in sections:
            layout.add_widget(Button(text=section, size_hint_y=None, height=100))
            
        return layout

if __name__ == "__main__":
    IMCIApp().run()
