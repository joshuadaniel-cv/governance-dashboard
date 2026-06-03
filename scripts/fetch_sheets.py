import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

SHEET_ID = '1nn9tlhMO4W0c6ho-dlrsHGKjC6WS6HEZ-PEFSTQAEWg'

# Use service account credentials from GitHub Secrets
# For now, we'll use gspread with public sheet access
try:
    gc = gspread.Client(auth=None)
    sh = gc.open_by_key(SHEET_ID)
    sheet_name = sh.title
    
    # Get all sheets
    sheets_list = [sheet.title for sheet in sh.worksheets()]
    
    data = {
        'sheet_name': sheet_name,
        'sheets': sheets_list
    }
    
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Fetched sheet: {sheet_name}")
except Exception as e:
    print(f"Error: {e}")
