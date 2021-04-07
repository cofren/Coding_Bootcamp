from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file('credentials2.json',scopes = SCOPES)

service = build('sheets', 'v4', credentials=creds)


# The ID and range of the spreadsheet to copy from.
spreadsheet_id = '12UJ_EumM5VTS5e4wdh3oEao8TIxx4dejX3rHD0pv1Os'
sheetId = 0

batch_update_spreadsheet_request_body = {
      "requests": [
    {
      "mergeCells": {
        "range": {
          "sheetId": sheetId,
          "startRowIndex": 0,
          "endRowIndex": 2,
          "startColumnIndex": 0,
          "endColumnIndex": 2
        },
        "mergeType": "MERGE_ALL"
      }
    },
    {
      "mergeCells": {
        "range": {
          "sheetId": sheetId,
          "startRowIndex": 2,
          "endRowIndex": 6,
          "startColumnIndex": 0,
          "endColumnIndex": 2
        },
        "mergeType": "MERGE_COLUMNS"
      }
    },
  ]
}

request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body)
response = request.execute()

print(response)

