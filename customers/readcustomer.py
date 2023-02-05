import mysql.connector


def readAllCustomers():
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")

        rows = cursor.fetchall()
        print("Total no. of records:", cursor.rowcount)
        for row in rows:
            print(row)

        cursor.close()
        conn.close()


def readOneCustomer(custId):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (custId))
        row = cursor.fetchone()
        if row is not None:
            print(row)


# readAllCustomers()

customerId = list(input("Enter the id of the customer:"))
readOneCustomer(customerId)
