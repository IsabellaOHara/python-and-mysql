import mysql.connector


def delete(companyId):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM companies WHERE company_id = %s" % companyId)

            conn.commit()
            print("Company deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


compId = int(input("Enter company id:"))
delete(compId)
