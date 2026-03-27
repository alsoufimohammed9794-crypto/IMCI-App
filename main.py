from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# إعداد لون خلفية مريح للعين
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class IMCILayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        # العنوان الرئيسي
        self.add_widget(Label(
            text="نظام التدبير المتكامل (IMCI) - اليمن",
            font_size='24sp',
            color=(0, 0.4, 0.2, 1),
            bold=True
        ))

        self.add_widget(Label(
            text="مرحباً بك دكتور محمد عبدالله\nابدأ بتقييم حالة الطفل الآن",
            halign='center',
            color=(0.2, 0.2, 0.2, 1)
        ))

        # أزرار الوظائف
        btn_assess = Button(
            text="تقييم حالة جديدة",
            size_hint=(1, 0.2),
            background_color=(0, 0.6, 0.3, 1)
        )
        self.add_widget(btn_assess)

        btn_guide = Button(
            text="دليل البروتوكول الوطني",
            size_hint=(1, 0.2),
            background_color=(0.1, 0.4, 0.8, 1)
        )
        self.add_widget(btn_guide)

class IMCIApp(App):
    def build(self):
        self.title = "IMCI Yemen"
        return IMCILayout()

if __name__ == "__main__":
    IMCIApp().run()
