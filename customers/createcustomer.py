import mysql.connector


def createCustomer(id, firstName, lastName, gender, email, complaints):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO customers VALUES(%s, %s, %s, %s, %s, %s)", (id, firstName, lastName,
                                                                                    gender, email, complaints))
            conn.commit()
            print("Customer created")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


custId = int(input("Enter customer id:"))
firstNm = input("Enter the first name:")
lastNm = input("Enter the last name:")
gendr = input("Enter the gender - M/F:")
emailaddress = input("Enter the email:")
complaint = int(input("Enter number of complaints:"))
createCustomer(custId, firstNm, lastNm, gendr, emailaddress, complaint)
