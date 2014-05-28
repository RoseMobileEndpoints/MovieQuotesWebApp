
from google.appengine.ext import ndb

# TODO: Convert this non-Endpoints version to use Endpoint Models!

class MovieQuote(ndb.Model):
    """ A movie quote and the title of the movie. """
    quote = ndb.StringProperty()
    movie = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    