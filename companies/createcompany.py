import mysql.connector


def createCompany(id, companyName, phoneNum):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO companies VALUES(%s, %s, %s)", (id, companyName, phoneNum))
            conn.commit()
            print("Company created")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


companyId = int(input("Enter company id:"))
compName = input("Enter the company name:")
phoneNo = input("Enter HQ phone number:")
createCompany(companyId, compName, phoneNo)

