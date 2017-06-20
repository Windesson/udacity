import webapp2


form= """
<form  action="">
  <label>
  One
  <input type="radio" name="q" value="one">
  </label>
  
  <label>
  Two
  <input type="radio" name="q" value="two">
  </label>
  
  <label>
  Three
  <input type="radio" name="q" value="three">
  </label>
  
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
http://localhost:8081/?q=on

"""