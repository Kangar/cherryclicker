import cherrypy
import os

static_dir = os.path.join(os.getcwd(), 'public')

class CherryClicker(object):
	@cherrypy.expose
	def indexx(self):
		return 'INDEX is here!!!'

	@cherrypy.expose
	def mypage(self):
		return 'MyPage!!'

cherrypy.quickstart(CherryClicker())