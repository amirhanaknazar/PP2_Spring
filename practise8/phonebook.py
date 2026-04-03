import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="12345678"
)

cur = conn.cursor()


def upsert(name, phone):
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Contact inserted/updated")


def delete(value):
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    print("Deleted if existed")


def insert_many(names, phones):
    cur.execute("CALL insert_many(%s, %s)", (names, phones))
    conn.commit()
    print("Bulk insert done")

def search(text):
    cur.execute("SELECT * FROM search_contacts(%s)", (text,))
    print(cur.fetchall())


def paginate(limit, offset):
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    print(cur.fetchall())

def menu():
    while True:
        print("""
1. Add / Update contact
2. Search contact
3. Delete contact
4. Bulk insert
5. Pagination
6. Exit
        """)

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            upsert(name, phone)

        elif choice == "2":
            text = input("Search: ")
            search(text)

        elif choice == "3":
            value = input("Name or phone: ")
            delete(value)

        elif choice == "4":
            names = input("Names (comma): ").split(",")
            phones = input("Phones (comma): ").split(",")
            insert_many(names, phones)

        elif choice == "5":
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            paginate(limit, offset)

        elif choice == "6":
            break


if __name__ == "__main__":
    menu()

    cur.close()
    conn.close()