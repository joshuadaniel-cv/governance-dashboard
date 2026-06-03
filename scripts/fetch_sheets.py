import gspread
import json

SHEET_ID = '1nn9tlhMO4W0c6ho-dlrsHGKjC6WS6HEZ-PEFSTQAEWg'

try:
    # Open public sheet without authentication
    gc = gspread.Client(auth=None)
    sh = gc.open_by_key(SHEET_ID)
    
    sheet_name = sh.title
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
    # Create empty data.json on error
    with open('data.json', 'w') as f:
        json.dump({'sheet_name': 'Error loading sheet', 'sheets': []}, f)
