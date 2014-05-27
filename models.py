
from google.appengine.ext import ndb

# TODO: Convert this non-Endpoints version to Endpoints!

class MovieQuote(ndb.Model):
    """ A movie quote and the title of the movie. """
    title = ndb.StringProperty()
    quote = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    