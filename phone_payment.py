from spreadsheet import Spreadsheet
from session import Session

def main():
    session = Session()
    session.start_session()
    creds = session.get_credentials()

    spreadsheet = Spreadsheet(creds)

    operation = int(input('Operations:\n1 - Read sheet\n2 - Update sheet\n'))
    if operation == 1:  
        values = spreadsheet.get_spreadsheet_values("A1:E12")
        for row in values:
            print(row)
    elif operation == 2:
        payment_one = int(input('Payment One: '))
        payment_two = int(input('Payment Two: '))
        month = int(input('Month: '))
        spreadsheet.insert_values_in_sheet(payment_one, payment_two, month)
    else:
        print('Invalid operation!')

if __name__ == '__main__':
    main()