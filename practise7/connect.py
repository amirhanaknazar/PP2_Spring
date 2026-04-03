import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="12345678"
    )

    print("Connected successfully!")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)