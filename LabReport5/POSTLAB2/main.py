from lzma import FORMAT_ALONE
import sqlite3
import datetime
con = sqlite3.connect('C:/Users/Marlon/Desktop/2nd Year/2nd Sem/SD/Laboratories/Lab no 5/post lab/2/SCG.db')
cursor = con.cursor()


def registration():
    print('')
    first_name = str(input("Enter firstname: "))
    middle_initial = str(input("Enter middile initial: "))
    last_name = str(input("Enter lastname: "))
    address = str(input("Enter address: "))
    city = str(input("Enter city: "))
    state = str(input("Enter state: "))
    postal = str(input("Enter postal code: "))
    telephone_number = str(input("Enter telephone number: "))
    email_address = str(input("Enter email address: "))

    user_input = """INSERT INTO renter
    (LAST_NAME, MIDDLE_INITIAL, FIRST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE_NUMBER, EMAIL_ADDRESS)
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(last_name, middle_initial, first_name, address, city, state, postal, telephone_number, email_address)

    cursor.execute(user_input)
    con.commit()
    print('Details recorded')
    rental_agreement()

def rental_agreement():

    condo_num = str(input("Please Select the Condo unit number: ")).upper()
    print("Registration Added")


    cursor.execute('SELECT CONDO_UNIT_NUMBER FROM property WHERE CONDO_UNIT_NUMBER = \''+condo_num+"\'")
    result = cursor.fetchone()

    temp = datetime.datetime.now()
    now = temp.strftime("%y-%m-%d")
    due = temp + datetime.timedelta(days=7)
    due_date = due.strftime("%y-%m-%d")
    if result:
            query = """INSERT INTO rental_agreement (RENTER_NUMBER, FIRST_NAME, MIDDLE_INITIAL, LAST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE_NUMBER) SELECT
            RENTER_ID, FIRST_NAME, MIDDLE_INITIAL, LAST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE_NUMBER 
            FROM (SELECT * from renter WHERE RENTER_ID = (SELECT MAX(RENTER_ID) FROM renter)); """
     
            query2 = """INSERT INTO rental_agreement(START_DATE_RENTAL, END_DATE_RENTAL)
            VALUES ('{}', '{}')""".format(now, due_date)

            query3 = """INSERT INTO rental_agreement(WEEKLY_RATE) SELECT WEEKLY_RATE FROM property WHERE CONDO_UNIT_NUMBER = 'condo_num' """

            cursor.execute(query)
            con.commit()

            print('Reservation recorded')


registration()