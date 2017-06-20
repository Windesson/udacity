import webapp2
from string import Template

form= Template("""
<form method="post">
  What is your bithday? 
  <br>
  <label>
    Month:
    <input type="text" name="month" value="$month" >
  </label>
  <label>
    Day: 
    <input type="text" name="day" value="$day">
  </label>
  <label>
    Year: 
    <input type="text" name="year" value="$year">
  </label>
  
  <div style="color:red;">$error</div>
  <br>
  <br>
  <input type="submit">
</form>
""")

happy_birthday = Template("""
Your birthday is on $month/$day/$year
""")

Opps ="""
Opps, Something went wrong!
""" 

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
    if day and day.isdigit():
        day = int(day)
        if(day>0 and day<= 32):
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if(year>1900 and year <= 2020):
            return year

def escape_html(data):
    escape = {'>':'&gt;', '<':'&lt;','\"':'&quot;','&': '&amp;'};  
    new_s = ""         
    # return s if not found in the dic or replace s
    for s in data:
        new_s += escape.get(s,s) 
        
    # python way    
    # return "".join(html_escape_table.get(c,c) for c in s)
    
    return new_s
        
        
class MainPage(webapp2.RequestHandler):
    def write_form(self, month="",day="", year="", error=False):
        message = "";
        if error:
            message = "You enter a invalid date! %s/%s/%s" % (month,day,year)
            
        return form.substitute(month=month,
                               day=day,
                               year=year,
                               error=message);

    def sing_birthday(self, month="",day="", year=""):
        return happy_birthday.substitute(month=month,
                                         day=day,
                                         year=year)
                 
    def get(self):
        self.response.write(self.write_form());
                           
    def post(self):
        
        try: 
            user_month = escape_html(self.request.POST['month'])
            user_day = escape_html(self.request.POST['day'])
            user_year = escape_html(self.request.POST['year'])
            
            month = valid_month(user_month)
            day  = valid_day(user_day)
            year = valid_year(user_year)
        
            if month and day and year: 
                self.response.write(
                 self.sing_birthday(month,
                                  day,
                                  year))
            else:           
                self.response.write(
                        self.write_form(user_month,
                                        user_day,
                                        user_year,
                                        True));
        except:
            self.response.write(Opps)
            
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8081')

if __name__ == '__main__':
    main()
    
"""
Advanced String Substitution

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string2 %({"nickname":nickname,"name":name})
    
#print sub_m("Mike", "Goose") 
# => "I'm Goose. My real name is Mike, but my friends call me Goose."
    
    
"""