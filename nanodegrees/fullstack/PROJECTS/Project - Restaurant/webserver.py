from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
import database_server as r

base_form = """
<html>
  <head>
  </head>
  <body>
    %s
  <body>
</html>"""

restaurantes_form = base_form % """
    <a href="/restaurants/new">Add a new restaurant</a>
    <br>
    <a href="/restaurants/delete">Delete a restaurant</a>
    <br>
    <ul>
      %s
    </ul>
""" 

new_form = base_form % """
    <a href="/restaurants">Return to restaurants</a>
    <br>
    <form enctype='multipart/form-data' method="post">
      Add Restaurant: <input type="text" name="newRestaurantName"><br>
      <input type="submit" value="Submit">
    </form>
    <br>
    %s
"""

del_form = base_form % """
    <a href="/restaurants">Return to restaurants</a>
    <br>
    <form enctype='multipart/form-data' method="post">
      Delete Restaurant: <input type="text" name="delRestaurantName" value="{name}"><br>
      <input type="submit" value="Submit">
    </form>
    <br>
"""

edit_form = base_form %  """
    <a href="/restaurants">Return to restaurants</a>
    <br>
    %s 
    <br>
    <form action="/restaurants/update" enctype='multipart/form-data' method="post">
      <input type="hidden" name="id" value="%s"><br>
      <input type="text" name="updateRestaurantName"><br>
      <input type="submit" value="Rename">
    </form>
    <br>
"""
iddel_form = base_form %  """
    <a href="/restaurants">Return to restaurants</a>
    <br>
    Are you sure you want to delete {name}
    <br>
    <form action="/restaurants/delete" enctype='multipart/form-data' method="post">
      <input type="hidden" name="delRestaurantName" value="{name}"><br>
      <input type="submit" value="Submit">
    </form>
    <br>
"""

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
             
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = restaurantes_form % r.get_restaurants()
                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/restaurants/new",0,16):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(new_form % "")
                return
            if self.path.endswith("/restaurants/delete",0,19):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(del_form.format(name=""))
                return
            if self.path.endswith("edit",-4):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                restaurant_id = self.path.split("/")[2]
                print "Get request to edit restaurant id: %s" % restaurant_id
                self.wfile.write(edit_form % r.get_restaurants(restaurant_id))
                return                
            if self.path.endswith("/delete"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()                
                restaurantIDPath = self.path.split("/")[2]
                output = iddel_form.format(name = r.get_restaurants(restaurantIDPath)[0])
                self.wfile.write(output)
                print output
                return                  
                
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    newrestaurant = messagecontent[0]
                    print "adding new restaurant:"+str(newrestaurant)
                    
                    # Adding restaurant 
                    status = r.set_restaurant(newrestaurant)
                    
                    # redirect 
                    self.send_response(301)
                    self.send_header("Location", "/restaurants/new?status=%s" % status)
                    self.end_headers()

            if self.path.endswith("/restaurants/delete"):

                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('delRestaurantName')
                    newrestaurant = messagecontent[0]
                    print "deleting restaurant:"+str(newrestaurant)
                    
                    # deleting restaurant 
                    status = r.delete_restaurant(newrestaurant)

                    # redirect 
                    self.send_response(301)
                    self.send_header("Location", "/restaurants")
                    self.end_headers()   
                    
            if self.path.endswith("/restaurants/update"):

                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    r_newName = fields.get('updateRestaurantName')[0]
                    r_id = fields.get('id')[0]
                    data = (r_newName,r_id)
                    print "updating %s id %s " % data
                    
                    # deleing restaurant 
                    status = r.update_restaurant(data)

                    # redirect 
                    self.send_response(301)
                    self.send_header("Location", "/restaurants")
                    self.end_headers()  
        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
