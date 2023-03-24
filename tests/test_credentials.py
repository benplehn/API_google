import os
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def test_credentials_exist():
    # Ensure that the credentials file exists
    credentials_file = os.path.join(os.getcwd(), 'resources/credentials.json')
    assert os.path.exists(credentials_file), 'Credentials file not found.'

def test_credentials_valid():
    # Ensure that the credentials are valid
    token_file = os.path.join(os.getcwd(), 'resources/token.json')
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    assert creds.valid, 'Invalid credentials.'
