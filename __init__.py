from flask import Blueprint,flash,redirect,url_for,session,render_template,Markup



class Youku(object):
	def __init__(self,app=None,**kwargs):
		if app:
			self.init_app(app)

	def init_app(self,app):
		self.register_blueprint(app)
		app.add_template_global(youku)

	def register_blueprint(self,app):
		module=Blueprint(
			"youku",
			__name__,
		)
		app.register_blueprint(module)
		return module

class Video(object):
	def __init__(self,video_id,cls="youku"):
		self.video_id=video_id
		self.cls=cls
	def render(self,*args,**kwargs):
		return render_template(*args,**kwargs)

	@property
	def html(self):
		return Markup(self.render('youku/video.html',video=self))

def youku(*args,**kwargs):
	video=Video(*args,**kwargs)
	return video.html