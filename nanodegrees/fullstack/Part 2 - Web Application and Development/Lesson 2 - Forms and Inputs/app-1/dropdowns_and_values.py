import webapp2


form= """
<form  action="">
  <select name="q">
     <option value="1">The number one</option>
     <option value="2">The number two</option>
     <option value="3">The number three</option>
  </select>
  
  <br>
  <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class Testhandler(webapp2.RequestHandler):
    def post(self):
        #q = self.request.get("q")
        #self.response.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', Testhandler),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
    
"""  checkbox
OUTPUT:
http://localhost:8081/?q=two
"""