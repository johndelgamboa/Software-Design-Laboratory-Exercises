import sqlite3

con = sqlite3.connect('CAT.db')
cursor = con.cursor()

def registration():

    class_number_enroll = int(input("Enter class number to enroll: "))
    last_name = str(input("Enter lastname: "))
    first_name = str(input("Enter firstname: "))
    address = str(input("Enter address: "))
    city = str(input("Enter city: "))
    state = str(input("Enter state: "))
    postal = str(input("Enter postal code: "))
    telephone_number = str(input("Enter telephone number: "))
    date_of_birth = str(input("Enter date of birth: "))
    date_today = str(input("Enter the Date today: "))


    user_input = """INSERT INTO part
    (LAST_NAME, FIRST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, TELEPHONE_NUMBER, DATE_OF_BIRTH)
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(last_name, first_name, address, city, state, postal, telephone_number, date_of_birth)

    cursor.execute(user_input)
    con.commit()
    
    if class_number_enroll == 1001:
        class_des = "Hiking"
        class_enroll = """INSERT INTO participant_class
                        (LAST_NAME, FIRST_NAME, CLASS_NUMBER, CLASS_DESCRIPTION, DATE_OF_CLASS)
                        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(last_name, first_name, class_number_enroll, class_des, date_today)

        class_list = """INSERT INTO class
                        (LAST_NAME, FIRST_NAME, CLASS_NUMBER, CLASS_DESCRIPTION, CLASS_DATE)
                        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(last_name, first_name, class_number_enroll, class_des, date_today)   

        cursor.execute(class_enroll)
        cursor.execute(class_list)
        con.commit()

    elif class_number_enroll == 1002:
        class_des = "Biking"
        class_enroll = """INSERT INTO participant_class
                        (LAST_NAME, FIRST_NAME, CLASS_NUMBER, CLASS_DESCRIPTION, DATE_OF_CLASS)
                        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(last_name, first_name, class_number_enroll, class_des, date_today)

        class_list = """INSERT INTO class
                        (LAST_NAME, FIRST_NAME, CLASS_NUMBER, CLASS_DESCRIPTION, CLASS_DATE)
                        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(last_name, first_name, class_number_enroll, class_des, date_today)   
   
                        
        cursor.execute(class_enroll)
        cursor.execute(class_list)
        con.commit()

    elif class_number_enroll == 1003:
        class_des = "Paddling"
        class_enroll = """INSERT INTO participant_class
                        (LAST_NAME, FIRST_NAME, CLASS_NUMBER, CLASS_DESCRIPTION, DATE_OF_CLASS)
                        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(last_name, first_name, class_number_enroll, class_des, date_today)

        class_list = """INSERT INTO class
                        (LAST_NAME, FIRST_NAME, CLASS_NUMBER, CLASS_DESCRIPTION, CLASS_DATE)
                        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(last_name, first_name, class_number_enroll, class_des, date_today)   
                  
        cursor.execute(class_enroll)
        cursor.execute(class_list)
        con.commit()

    cursor.close


def participant_list():
    cursor.execute("SELECT * FROM part ")
    data = cursor.fetchall()

    for row in data:
        print('\n', row)

def participant_class_list():
    cursor.execute("SELECT * FROM participant_class ")
    data = cursor.fetchall()

    for row in data:
        print('\n', row)

def class_list():
    cursor.execute("SELECT * FROM class ")
    data = cursor.fetchall()

    for row in data:
        print('\n', row)

def avail_class():
    cursor.execute("SELECT * FROM adventure_class ")
    data = cursor.fetchall()

    for row in data:
        print('\n', row)

print('')
print('-----Welcome to Colonial Adventure Tours-----')
print('')
print('[1] Register to a class')
print('[2] view class list')
print('[3] view participants/class')
user_choice = int(input("-->"))
print('\n')
if user_choice == 1:
    registration()

if user_choice == 2:
    avail_class   

if user_choice == 3:
    class_list


    

