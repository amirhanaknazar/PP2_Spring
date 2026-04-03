import psycopg2
import csv


def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="12345678"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")


def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def search():
    text = input("Search name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        ('%' + text + '%',)
    )

    print(cur.fetchall())

    cur.close()
    conn.close()


def update():
    old = input("Old name: ")
    new = input("New name: ")
    phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        UPDATE phonebook
        SET name=%s, phone=%s
        WHERE name=%s
    """, (new, phone, old))

    conn.commit()
    cur.close()
    conn.close()

    print("Updated!")

def delete():
    val = input("Name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name=%s OR phone=%s",
        (val, val)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")


def import_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()

    print("CSV imported!")


def menu():
    while True:
        print("\n=== PHONEBOOK ===")
        print("1. Add contact")
        print("2. Show all")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Import CSV")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            import_csv()
        elif choice == "7":
            break


if __name__ == "__main__":
    create_table()
    menu()