import cherrypy
import os

STATIC_DIR = os.path.join(os.getcwd(), 'public')

class CherryClicker(object):
	@cherrypy.expose
	def index(self):
		cherrypy.response.headers['Content-Type'] = 'text/html'
		return '(index page goes here)<br />' + \
		'<a href="hello.txt">link to static file</a>'

	@cherrypy.expose
	def mypage(self):
		cherrypy.response.headers['Content-Type']= 'text/html'
		return 'MyPage'

cherrypy.server.socket_port = 8080
cherrypy.server.socket_host = '0.0.0.0'

conf = {
	'/': {
		'tools.staticdir.on' : True,
		'tools.staticdir.dir' : STATIC_DIR,
	}
}

cherrypy.quickstart(CherryClicker(), config=conf)
