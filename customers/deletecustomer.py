import mysql.connector


def delete(custId):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM customers WHERE customer_id = %s" % custId)

            conn.commit()
            print("Customer deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


customerId = int(input("Enter customer id:"))
delete(customerId)
