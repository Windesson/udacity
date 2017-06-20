import webapp2
import os
import cgi

def escape_html(data):
    return cgi.escape(data, quote = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):               
    def get(self):
        self.write("Hello, Udacity!");
                           
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
