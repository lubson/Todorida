import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mygtd.lib.base import BaseController, render
import mygtd.lib.helpers as h


log = logging.getLogger(__name__)

class AccountController(BaseController):

    def signin(self):
        if not request.environ.get('REMOTE_USER'):
            # This triggers the AuthKit middleware into displaying the sign-in form
            abort(401)
        else:
            response.status_int = 302
            response.headers['location'] = h.url_for(controller='page',action='inbox')
            return 'Moved temporarily'

    def signout(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        return "<p>You have been signed out</p><a href=\"http://localhost:5000/account/signin\">Sign in</a>"
