import os.path
from google.oauth2.credentials import Credentials

def test_credentials_exist():
    # Ensure that the credentials file exists
   assert os.path.exists('../resources/credentials.json'), 'Credentials file not found.'


def test_credentials_valid():
    # Ensure that the credentials are valid
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    assert creds.valid, 'Invalid credentials.'
