# Kivy Template

A blank Kivy project. You can use these code files as a template for create a new screen.

* think of a name for your page
* rename `mypagename.kv` to your new name
 * this file should be all in lower case and contain no spaces
* rename `MyPageName` in the `main.py` and the `.kv` file
 * you may use mixed case here to separate words

## Example

I want to create a new title page, so I choose the name `Title`.
First I rename `mypagename.kv` to `title.kv`. Then in my editor (you can use Spyder for this) I change `MyPageName` to `Title` everywhere in the `.py` file and `.kv` file.

After which my `main.py` file will look like this:

~~~
from kivy.app import App
from kivy.uix.widget import Widget

class TitleScreen(Widget):
    pass

class TitleApp(App):
    def build(self):
        return TitleScreen()

if __name__ == '__main__':
    TitleApp().run()
~~~

and my `title.kv` file will look like this:

~~~
#:kivy 1.0.9

<TitleScreen>:
    Label:
        center_x: root.width / 2
        center_y: root.height / 2
        text: "My page"
~~~
