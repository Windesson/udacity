import webapp2

form= """
<form action="http://www.google.com/search">
  <input name="q">
  <input type="submit" name="">
</form>
"""

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, webapp2!')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8080')

if __name__ == '__main__':
    main()