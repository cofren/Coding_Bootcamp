from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

SECRET_FILE = 'credentials2.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

creds = service_account.Credentials.from_service_account_file(SECRET_FILE,scopes = SCOPES)

service = build(API_NAME, API_VERSION, credentials=creds)

# Copy a file into multiple folders
source_file_id = '12UJ_EumM5VTS5e4wdh3oEao8TIxx4dejX3rHD0pv1Os'
folder_ids = [
  '1Eg3VcATL7VIn2z2p6TaiTNg1Avbrn9IY',
  '1Ju2R9K-9PpGQZjmLz1LTTxyV4TLn_02p']
file_metadata = {
  'name': 'TempTest',
  'parents': folder_ids,
}

service.files().copy(
  fileId = source_file_id,
  body = file_metadata
).execute()

# # Call the Drive v3 API
# results = service.files().list(
#     pageSize=10, fields="nextPageToken, files(id, name)").execute()
# items = results.get('files', [])

# if not items:
#     print('No files found.')
# else:
#     print('Files:')
#     for item in items:
#         print(u'{0} ({1})'.format(item['name'], item['id']))
