import csv
import json
from connect import connect


def create_group(cur, name):
    cur.execute("SELECT id FROM groups WHERE name=%s", (name,))
    g = cur.fetchone()
    if g:
        return g[0]
    cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (name,))
    return cur.fetchone()[0]


def add_contact():
    conn = connect()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday: ")
    group = input("Group: ")
    phone = input("Phone: ")
    ptype = input("Type: ")

    gid = create_group(cur, group)

    cur.execute("""
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES(%s,%s,%s,%s)
        ON CONFLICT (name) DO NOTHING
        RETURNING id
    """, (name, email, birthday, gid))

    r = cur.fetchone()

    if r:
        cid = r[0]
    else:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        cid = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO phones(contact_id,phone,type)
        VALUES(%s,%s,%s)
    """, (cid, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()
    print("СДЕЛАНО")


def import_csv(file):
    conn = connect()
    cur = conn.cursor()

    with open(file, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)

        for i in r:
            gid = create_group(cur, i["group_name"])

            cur.execute("""
                INSERT INTO contacts(name,email,birthday,group_id)
                VALUES(%s,%s,%s,%s)
                ON CONFLICT (name) DO NOTHING
            """, (i["name"], i["email"], i["birthday"], gid))

            cur.execute("SELECT id FROM contacts WHERE name=%s", (i["name"],))
            cid = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO phones(contact_id,phone,type)
                VALUES(%s,%s,%s)
            """, (cid, i["phone"], i["phone_type"]))

    conn.commit()
    cur.close()
    conn.close()
    print("СДЕЛАНО")


def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name,c.email,c.birthday,g.name,p.phone,p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
    """)

    for i in cur.fetchall():
        print(i)

    cur.close()
    conn.close()
    print("СДЕЛАНО")


def search():
    conn = connect()
    cur = conn.cursor()

    q = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (q,))

    for i in cur.fetchall():
        print(i)

    cur.close()
    conn.close()
    print("СДЕЛАНО")


def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name,c.email,c.birthday,g.name,p.phone,p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
    """)

    data = []
    for i in cur.fetchall():
        data.append({
            "name": i[0],
            "email": i[1],
            "birthday": str(i[2]),
            "group": i[3],
            "phone": i[4],
            "type": i[5]
        })

    with open("contacts.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

    cur.close()
    conn.close()
    print("СДЕЛАНО")


def import_json():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.json",encoding="utf-8") as f:
        data = json.load(f)

    for i in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s",(i["name"],))
        ex = cur.fetchone()

        if ex:
            cur.execute("DELETE FROM contacts WHERE name=%s",(i["name"],))

        gid = create_group(cur,i["group"])

        cur.execute("""
            INSERT INTO contacts(name,email,birthday,group_id)
            VALUES(%s,%s,%s,%s)
            RETURNING id
        """,(i["name"],i["email"],i["birthday"],gid))

        cid = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO phones(contact_id,phone,type)
            VALUES(%s,%s,%s)
        """,(cid,i["phone"],i["type"]))

    conn.commit()
    cur.close()
    conn.close()
    print("СДЕЛАНО")


def filter_group():
    conn = connect()
    cur = conn.cursor()

    g = input("Group: ")

    cur.execute("""
        SELECT c.name,c.email,c.birthday,g.name,p.phone,p.type
        FROM contacts c
        JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
        WHERE g.name ILIKE %s
    """,(g,))

    for i in cur.fetchall():
        print(i)

    cur.close()
    conn.close()
    print("СДЕЛАНО")


def sort_contacts():
    conn = connect()
    cur = conn.cursor()

    print("1 name 2 birthday 3 created")

    c = input("Choose: ")

    if c=="1":
        o="c.name"
    elif c=="2":
        o="c.birthday"
    else:
        o="c.created_at"

    cur.execute(f"""
        SELECT c.name,c.email,c.birthday,g.name,p.phone,p.type,c.created_at
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
        ORDER BY {o}
    """)

    for i in cur.fetchall():
        print(i)

    cur.close()
    conn.close()
    print("СДЕЛАНО")


def pagination():
    conn = connect()
    cur = conn.cursor()

    limit=2
    offset=0

    while True:
        cur.execute("""
            SELECT c.name,c.email,c.birthday,g.name,p.phone,p.type
            FROM contacts c
            LEFT JOIN groups g ON c.group_id=g.id
            LEFT JOIN phones p ON c.id=p.contact_id
            ORDER BY c.name
            LIMIT %s OFFSET %s
        """,(limit,offset))

        rows=cur.fetchall()

        for i in rows:
            print(i)

        cmd=input("next/prev/quit: ")

        if cmd=="next":
            offset+=limit
        elif cmd=="prev":
            offset=max(0,offset-limit)
        else:
            break

    cur.close()
    conn.close()
    print("СДЕЛАНО")


def main():
    while True:
        print("1 add")
        print("2 csv")
        print("3 show")
        print("4 search")
        print("5 export")
        print("6 import")
        print("7 filter")
        print("8 sort")
        print("9 pagination")
        print("10 exit")

        c=input("Choose: ")

        if c=="1":
            add_contact()
        elif c=="2":
            import_csv("contacts.csv")
        elif c=="3":
            show_contacts()
        elif c=="4":
            search()
        elif c=="5":
            export_json()
        elif c=="6":
            import_json()
        elif c=="7":
            filter_group()
        elif c=="8":
            sort_contacts()
        elif c=="9":
            pagination()
        else:
            break


main()