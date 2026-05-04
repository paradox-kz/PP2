import psycopg2
from connect import get_connection
import csv

conn = get_connection()
cur = conn.cursor()


def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    cur.execute(
        "INSERT INTO contacts(name,email,birthday) VALUES(%s,%s,%s)",
        (name, email, birthday)
    )
    conn.commit()


def add_phone():
    name = input("Name: ")
    phone = input("Phone: ")
    ptype = input("Type(home/work/mobile): ")

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()


def move_group():
    name = input("Name: ")
    group = input("Group: ")

    cur.execute("CALL move_to_group(%s,%s)", (name, group))
    conn.commit()


def search():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for row in cur.fetchall():
        print(row)


def filter_group():
    g = input("Group: ")
    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups gr ON c.group_id = gr.id
        WHERE gr.name = %s
    """, (g,))
    print(cur.fetchall())


def paginate():
    offset = 0
    limit = 3

    while True:
        cur.execute("""
            SELECT c.name, c.email, p.phone
            FROM contacts c
            LEFT JOIN phones p ON c.id = p.contact_id
            LIMIT %s OFFSET %s
            """, (limit, offset))

        rows = cur.fetchall()

        if not rows:
            print("No more contacts.")
        else:
            print("\n--- Contacts ---")
            for i, row in enumerate(rows, start=1):
                phone = row[2] if row[2] else "No phone"
                print(f"{i}. {row[0]} | {row[1]} | {phone}")

        cmd = input("next/prev/quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        elif cmd == "quit":
            break


def export_json():
    import json
    cur.execute("""
        SELECT c.name, c.email, p.phone, g.name
        FROM contacts c
        LEFT JOIN phones p ON c.id = p.contact_id
        LEFT JOIN groups g ON c.group_id = g.id
    """)
    data = cur.fetchall()

    with open("data.json", "w") as f:
        json.dump(data, f)


def import_csv():
    import csv

    print("Import mode:")
    print("1 - skip duplicates")
    print("2 - overwrite duplicates")
    print("3 - merge")

    mode = input("Choose (1/2/3): ")

    with open("contacts.csv") as f:
        reader = csv.reader(f)

        for row in reader:

            if len(row) < 2:
                print("❌ Skipping invalid row:", row)
                continue

            # --- базовые поля ---
            name = row[0]
            email = row[1]

            # --- optional ---
            birthday = row[2] if len(row) > 2 else None
            group = row[3] if len(row) > 3 else "Other"
            phone = row[4] if len(row) > 4 else None
            ptype = row[5] if len(row) > 5 else "mobile"

            # --- контакт ---
            cur.execute(
                "SELECT id FROM contacts WHERE name=%s AND email=%s",
                (name, email)
            )
            result = cur.fetchone()

            if result:
                contact_id = result[0]

                if mode == "1":
                    continue

                elif mode == "2":
                    cur.execute("""
                        UPDATE contacts
                        SET birthday=%s
                        WHERE id=%s
                    """, (birthday, contact_id))

            else:
                cur.execute("""
                    INSERT INTO contacts(name,email,birthday)
                    VALUES(%s,%s,%s)
                    RETURNING id
                """, (name, email, birthday))
                contact_id = cur.fetchone()[0]

            # --- группа ---
            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            group_res = cur.fetchone()

            if group_res:
                group_id = group_res[0]
            else:
                cur.execute(
                    "INSERT INTO groups(name) VALUES(%s) RETURNING id",
                    (group,)
                )
                group_id = cur.fetchone()[0]

            cur.execute(
                "UPDATE contacts SET group_id=%s WHERE id=%s",
                (group_id, contact_id)
            )

            # --- телефон ---
            if phone:
                cur.execute("""
                    SELECT id FROM phones
                    WHERE contact_id=%s AND phone=%s
                """, (contact_id, phone))

                if not cur.fetchone():
                    cur.execute("""
                        INSERT INTO phones(contact_id, phone, type)
                        VALUES(%s,%s,%s)
                    """, (contact_id, phone, ptype))

        conn.commit()
        print("✅ Flexible import finished")


def menu():
    while True:
        print("\n1.Add Contact")
        print("2.Add Phone")
        print("3.Move Group")
        print("4.Search")
        print("5.Filter Group")
        print("6.Pagination")
        print("7.Export JSON")
        print("8.Import CSV")
        print("9.Exit")

        ch = input(">> ")

        if ch == "1": add_contact()
        elif ch == "2": add_phone()
        elif ch == "3": move_group()
        elif ch == "4": search()
        elif ch == "5": filter_group()
        elif ch == "6": paginate()
        elif ch == "7": export_json()
        elif ch == "8": import_csv()
        elif ch == "9": break


menu()