import cherrypy
	  
class CherryClicker(object):
    def index(self):
        return "Welcome to Cherry Clicker!"
    index.exposed = True

cherrypy.quickstart(CherryClicker())