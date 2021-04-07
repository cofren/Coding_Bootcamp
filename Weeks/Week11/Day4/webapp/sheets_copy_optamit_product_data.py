from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file('credentials2.json',scopes = SCOPES)

# The ID and range of the spreadsheet to copy from.
COPYFROM_SPREADSHEET_ID = '1YEgHxj2pUdJq0pc8eeMfz92-LuCwpeijOnZ44bsIj9k'
COPYFROM_RANGE_NAME = 'MASTER!A1:DN'

# The ID and range of the spreadsheet to copy to.
COPYTO_SPREADSHEET_ID = '1y-ZcYH3XyYeiz9b2AzTTJXMuH0e3WxfLNkOKGc6u9wE'
COPYTO_RANGE_NAME = 'Sheet2!A1'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

# Copy
copy = sheet.values().get(spreadsheetId=COPYFROM_SPREADSHEET_ID,
                                range=COPYFROM_RANGE_NAME).execute()

copy_values = copy.get("values", [])
print(copy_values)

# Paste
paste = sheet.values().update(spreadsheetId=COPYTO_SPREADSHEET_ID,
                                    range=COPYTO_RANGE_NAME, valueInputOption="USER_ENTERED", body={"values": copy_values}).execute()

    
print(paste)

