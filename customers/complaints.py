import mysql.connector


def addComplaint(custId):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()

        try:
            cursor.execute("UPDATE customers SET number_of_complaints = number_of_complaints + 1 WHERE customer_id = %s", (custId))
            conn.commit()
            print("New complaint added")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


customerId = list(input("Enter the id of the customer:"))
addComplaint(customerId)
