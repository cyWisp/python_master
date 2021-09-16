#!/usr/bin/env python
class Classy:
    def visible(self):
        print("visible")
    def __hidden(self):
        print("hidden")

object_1 = Classy()
object_1.visible()

try:
    object_1.hidden()
except:
    print("failed")

object_1._Classy__hidden()