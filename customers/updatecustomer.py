import mysql.connector


def updateFirstName(custId, firstName):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE customers SET first_name = %s WHERE customer_id = %s", (firstName, custId))
            conn.commit()
            print("Customer first name updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def updateLastName(custId, lastName):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE customers SET last_name = %s WHERE customer_id = %s", (lastName, custId))
            conn.commit()
            print("Customer last name updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def updateGender(custId, gender):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE customers SET gender = %s WHERE customer_id = %s", (gender, custId))
            conn.commit()
            print("Customer gender updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def updateEmail(custId, email):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE customers SET email_address = %s WHERE customer_id = %s", (email, custId))
            conn.commit()
            print("Customer email updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


customerId = int(input("Enter customer id:"))
# fname = input("Enter new first name:")
# updateFirstName(customerId, fname)

# lname = input("Enter new last name:)
# updateLastName(customerId, lname)

# gend = input("Enter the gender M/F:")
# updateGender(customerId, gend)

# emailAddress = input("Enter the email address:")
# updateEmail(customerId, emailAddress)



