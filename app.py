import os
import tornado.ioloop
import tornado.web
import tornado.log
import urllib.parse
import requests
import json
from jinja2 import \
  Environment, PackageLoader, select_autoescape
ENV = Environment(
  loader=PackageLoader('myapp', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])
)
PORT = int(os.environ.get('PORT', '8888'))

class TemplateHandler(tornado.web.RequestHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    self.write(template.render(**context))

class MainHandler(TemplateHandler):
  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("index.html", {})

class CalcHandler(TemplateHandler):
    def post(self):
        salary = int(self.get_body_argument('salary'))
        salarymen = salary/.79
        result = salarymen - salary
        self.render_template("calc-result.html", {'result':result, 'salarymen': salarymen})

def make_app():
    return tornado.web.Application([
    (r"/", MainHandler),
    (r"/calculator", CalcHandler),
    (
      r"/static/(.*)",
      tornado.web.StaticFileHandler,
      {'path': 'static'}
    ),
    ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(PORT, print('Server started on localhost:' + str(PORT)))
    tornado.ioloop.IOLoop.current().start()