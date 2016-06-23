from system.core.controller import *

from time import gmtime, strftime

class Times(Controller):
    def __init__(self, action):
        super(Times, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        #self.load_model('WelcomeModel')
        #self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        date = strftime("%a, %d %b %Y")
        time = strftime('%H:%M:%S')
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html', date=date, time=time)
