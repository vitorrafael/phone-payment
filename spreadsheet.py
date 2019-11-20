from googleapiclient.discovery import build
import os


class Spreadsheet:
    '''
        Object that represents a spreadsheet and has
        methods to visualize a sheet and insert values
        in a sheet
    '''

    def __init__(self, creds):
        self.service = build('sheets', 'v4', credentials=creds)
        self.sheet = self.service.spreadsheets()
        self.SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

    def get_spreadsheet_values(self, range):
        ''' Get the spreadsheet values within a certain range'''
        result = self.sheet.values().get(
            spreadsheetId=self.SPREADSHEET_ID,
            range=range
        ).execute()
        values = result.get('values', [])
        return values

    def insert_values_in_sheet(self, payment_one, payment_two, month):
        ranges = {
            11: "B2:C2",
            12: "B3:C3",
            1: "B4:C4",
            2: "B5:C5",
            3: "B6:C6",
            4: "B7:C7",
            5: "B8:C8",
            6: "B9:C9",
            7: "B10:C10",
            8: "B11:C11",
            9: "B12:C12",
        }

        range = ranges[month]
        values = [[f"${payment_one}", f"${payment_two}"]]

        body = {'values': values}

        result = self.sheet.values().update(
            spreadsheetId=self.SPREADSHEET_ID, range=range,
            valueInputOption="USER_ENTERED", body=body
        ).execute()
