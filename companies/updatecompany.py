import mysql.connector


def updateCompanyName(companyId, companyName):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE companies SET company_name = %s WHERE company_id = %s", (companyName, companyId))
            conn.commit()
            print("Company name updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


def updateCompanyPhoneNum(companyId, companyPhoneNum):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE companies SET hq_phone_number = %s WHERE company_id = %s", (companyPhoneNum,
                                                                                               companyId))
            conn.commit()
            print("Company phone number updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


compId = int(input("Enter company id:"))
# cname = input("Enter new company name:")
# updateCompanyName(compId, cname)

phoneNum = input("Enter new phone number:")
updateCompanyPhoneNum(compId, phoneNum)

