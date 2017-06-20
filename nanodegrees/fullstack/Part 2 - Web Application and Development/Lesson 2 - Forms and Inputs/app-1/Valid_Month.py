import webapp2
from string import Template

form= """
<form method="post">
  What is your bithday? <br>
  <label>
  Month:
  <input type="text" name="month" >
  </label>
  
  <label>
  Day: 
  <input type="text" name="day" >
  </label>
  
  <label>
  Year: 
  <input type="text" name="year">
  </label>
  
  <br>
  <input type="submit">
</form>
"""

happy_birthday = Template("""
Your birthday is on $month/$day/$year
""")

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
#
# Jan : January
month_abbvs = dict((m[:3].lower(), m) for m in months)
          
def valid_month(month):
    if month:
       short_month = month[:3].lower();
       return month_abbvs.get(short_month)
 
def valid_day(day):
    # parse to int
    try:
        int_day = int(day)
        if(int_day>0 and int_day<32):
            return int_day
    except ValueError:
        pass
      
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        self.month = self.request.POST['month']
        self.day = self.request.POST['day']
        self.year = self.request.POST['year']
        
        self.month = valid_month(self.month)
        self.day  = valid_day(self.day)
        
        self.response.write(#self.request)
                happy_birthday.substitute(month=self.month,
                                          day=self.day,
                                          year=self.year))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()