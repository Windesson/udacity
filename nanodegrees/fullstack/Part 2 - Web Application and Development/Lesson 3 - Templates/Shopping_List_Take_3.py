import webapp2
import jinja2
import cgi
import os

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


def escape_html(data):
    return cgi.escape(data, quote = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **params):
        self.write(self.render_str(template, **params))

class MainPage(Handler):               
    def get(self):
        template = "shopping_list.html"
        items_raw = self.request.GET.getall('food')
        items_list = []
        
        for item in items_raw:
            items_list.append(escape_html(item)) 
        
        self.render(template,items=items_list)


                           
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
