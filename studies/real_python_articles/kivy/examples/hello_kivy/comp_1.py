#!/usr/bin/env python
from kivy.app Import app
from kivy.uix.label import Label
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        label = Label(text='This is a label',
                    size_hint = (.5, .5),
                    pos_hint = {'center_x': .5, 'center_y': .5},
                    )
        img = Image(source = './images/kali_R.jpg',
                        size_hint = (.5, .5),
                        pos_hint = ('center_x': .5, 'center_y': .5),
                        )
        