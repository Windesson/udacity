import webapp2


form= """
<form action="/testform">
  <input name="q">
  <input type="submit" name="">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class Testhandler(webapp2.RequestHandler):
    def get(self):
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
    
"""
OUTPUT:
GET /testform?q=oi HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.8
Connection: keep-alive
Content-Length: 0
Content-Type: 
Host: localhost:8081
Referer: http://localhost:8081/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3109.0 Safari/537.36
"""