import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


class Session:

    def __init__(self):
        self.creds = None
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    def start_session(self):
        'Starts the Google API session'

        # The session tokens are already stored in the computer
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        # If the credentials are not stored in the computer or they aren't valid
        if not self.creds or not self.creds.valid:
            # If the credentials have expired, refresh them
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:  # Creds are still valid
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            
            # Stores the credentials in token.pickle
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

    def get_credentials(self):
        return self.creds