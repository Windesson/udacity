import webapp2


form= """
<form  method="post">
  <input type="text" name="q">
  <br>
  <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)


app = webapp2.WSGIApplication([
    ('/', MainPage),
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