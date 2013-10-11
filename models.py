
from google.appengine.ext import ndb

class MovieQuote(ndb.Model):
    movie_title = ndb.StringProperty()
    quote = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    