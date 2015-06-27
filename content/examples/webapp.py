from circuits.web import Server, Controller


class Root(Controller):

    def index(self):
        return "Hello World!"

(Server(("0.0.0.0", 9000)) + Root()).run()
