from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1Ut5-v9SVePAnWiK9QFTdoaHNm16UALgx53hkHaoWwIE'


# [string] -> google-api-object
def initialize_connection(creds_json_file = 'credentials.json'):
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
                creds_json_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    return service


def build_data():
    return [["afdf", "b"],  [11 , 22, 32]]



def main():
    service = initialize_connection()
    sheet = service.spreadsheets()

    dataToInsert = build_data()

    sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range="A1:Z").execute()

    result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                         range="A1", valueInputOption='USER_ENTERED',
                         body = { 'values' :  dataToInsert }).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))



if __name__ == '__main__':
    main()
annas-air:Downloads annalester$ cat sheets-import.py 
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1Ut5-v9SVePAnWiK9QFTdoaHNm16UALgx53hkHaoWwIE'


# [string] -> google-api-object
def initialize_connection(creds_json_file = 'credentials.json'):
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
                creds_json_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    return service


def build_data():
    return [["a", "b", "c"],  [1 , 2, 3]]



def main():
    service = initialize_connection()
    sheet = service.spreadsheets()

    dataToInsert = build_data()

    sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range="A1:Z").execute()

    result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                         range="A1", valueInputOption='USER_ENTERED',
                         body = { 'values' :  dataToInsert }).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))



if __name__ == '__main__':
    main()
