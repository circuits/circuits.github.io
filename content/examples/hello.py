from __future__ import print_function

from circuits import Component, Event


class hello(Event):
    """hello Event"""


class App(Component):

    def hello(self):
        print("Hello World!")

    def started(self, component):
        self.fire(hello())
        raise SystemExit(0)

App().run()
