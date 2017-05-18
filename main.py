from kivy.app import App
from kivy.uix.widget import Widget

class MyPageNameScreen(Widget):
    pass

class MyPageNameApp(App):
    def build(self):
        return MyPageNameScreen()


if __name__ == '__main__':
    MyPageNameApp().run()
