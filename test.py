import webapp2
import numpy as np

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(np.random.rand())


app = webapp2.WSGIApplication([('/',MainPage),
                               ],
                              debug=True)
