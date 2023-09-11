import kivy
from kivy import Logger
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

kivy.require('2.0.0')


class MyScreenManager(ScreenManager):
    pass


class MyScreen(Screen):
    pass


class AddButton(Button):
    pass

    def click(self):
        Logger.info(self.text)
        new_label = Label()
        new_label.text = "bar"
        App.get_running_app().root.ids.button_grid.add_widget(new_label)


class MyApp(App):
    def build(self):
        return MyScreen()


if __name__ == '__main__':
    MyApp().run()
