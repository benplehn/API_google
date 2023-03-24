from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Slides API.
    Prints the number of slides and elements in a presentation with a specified name.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../resources/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('slides', 'v1', credentials=creds)

        # Call the Slides API to search for presentations by name
        presentation_name = "DE OECHSLER: One-pager on data analytics"
        query = "name='" + presentation_name + "'"
        results = service.presentations().list(q=query, fields="presentations(id, title)").execute()
        presentations = results.get("presentations")

        # Get the presentation ID if a presentation with the specified name was found
        presentation_id = None
        if presentations:
            presentation = presentations[0]
            presentation_id = presentation.get("id")

        # If a presentation with the specified name was found, retrieve its details
        if presentation_id:
            presentation = service.presentations().get(
                presentationId=presentation_id).execute()
            slides = presentation.get('slides')

            print('The presentation "{}" contains {} slides:'.format(presentation_name, len(slides)))
            for i, slide in enumerate(slides):
                print('- Slide #{} contains {} elements.'.format(
                    i + 1, len(slide.get('pageElements'))))
        else:
            print("No presentation was found with the name '{}'.".format(presentation_name))

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
