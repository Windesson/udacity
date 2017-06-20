import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def rot13_calc(text):
    new_text = ""
    for s in text:
        dec_s = ord(s)
        
        # Uppercase senario
        if dec_s >= 65 and dec_s <= 90:
            rot13_s = dec_s + 13;
            if rot13_s > 90:
                new_text += chr(rot13_s - 90 + 64)
            else:
                 new_text += chr(rot13_s)

        # Lowercase senario 
        elif dec_s >= 97 and dec_s <= 122:
            rot13_s = dec_s + 13;
            if rot13_s > 122:
                new_text += chr(rot13_s - 122 + 96)
            else:
                 new_text += chr(rot13_s)                
        else:
          new_text += s  
            
    return new_text    
    
    
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
        items = []
        
        for item in items_raw:
            items.append(item) 
        
        self.render(template,items=items)

class FizzBuzz(Handler):
    def get(self):
        template = "fizzBuzz.html"
        n = 0;
        
        try:
            n = self.request.GET['n']
        except:
            pass
        
        self.render(template, n = n)

class ROT13(Handler):
    template = "rot13.html"
    
    def get(self):
        self.render(ROT13.template)
        
    def post(self):
        text = "";
        
        try:
            text = self.request.POST['text']
        except:
            pass
        
        text = rot13_calc(text)
        self.render(ROT13.template, text = text)

                           
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fizzbuzz', FizzBuzz),
    ('/rot13', ROT13),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
