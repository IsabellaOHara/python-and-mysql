import mysql.connector


def readAllCompanies():
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM companies")

        rows = cursor.fetchall()
        print("Total no. of records:", cursor.rowcount)
        for row in rows:
            print(row)

        cursor.close()
        conn.close()


def readOneCustomer(companyId):
    conn = mysql.connector.connect(host='localhost', database='sales', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to Sales DB")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM companies WHERE company_id = %s", (companyId))
        row = cursor.fetchone()
        if row is not None:
            print(row)


# readAllCompanies()

compId = list(input("Enter the company id:"))
readOneCustomer(compId)

