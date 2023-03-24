import os.path
from google.oauth2.credentials import Credentials
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']
   
def test_credentials_exist():
    # Ensure that the credentials file exists
   assert os.path.exists('/Users/benjaminplehn/API_ftrprf/resources/resources.json'), 'Credentials file not found.'


def test_credentials_valid():
    # Ensure that the credentials are valid
    creds = Credentials.from_authorized_user_file('/Users/benjaminplehn/API_ftrprf/resources/token.json', SCOPES)
    assert creds.valid, 'Invalid credentials.'
