from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file('credentials2.json',scopes = SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '12UJ_EumM5VTS5e4wdh3oEao8TIxx4dejX3rHD0pv1Os'
SAMPLE_RANGE_NAME = 'Sheet1!A1:C'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()

values = result.get("values", [])
print(values)

test_list = [["Hello",5],["DuDu",7,"blabla","HAMMER!!!"],["und noch eins!",True]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Sheet2!A1", valueInputOption="USER_ENTERED", body={"values": test_list}).execute()
    
print(request)

