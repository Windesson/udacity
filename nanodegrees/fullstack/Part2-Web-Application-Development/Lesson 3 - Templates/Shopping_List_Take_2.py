import webapp2
import jinja2
import cgi


form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

hidden_html = """
<input type="hidden" name="food" value="%s" >
"""

item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""


def escape_html(data):
    return cgi.escape(data, quote = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):               
    def get(self):
        output = form_html
        items = self.request.GET.getall('food')
        output_hidden = ""          
        output_item = ""
        output_list = ""
        
        for item in items:
            output_hidden += hidden_html % item
            output_item += item_html % item
        
        output = output % output_hidden
        output_list = shopping_list_html % output_item
        
        output += output_list;
        self.write(output);
                           
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
