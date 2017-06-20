import webapp2


form= """
<form method="post" action="/testform">
  <input name="q">
  <input type="submit" name="">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class Testhandler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get("q")
        self.response.write(q)
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', Testhandler),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
    
"""
OUTPUT:
    
    405 Method Not Allowed

The method POST is not allowed for this resource. 
    
"""