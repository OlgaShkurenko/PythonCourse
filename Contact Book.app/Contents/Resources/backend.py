import sqlite3

def connect():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY, name TEXT, organization TEXT, phone TEXT, contact_group TEXT)")
    conn.commit()
    conn.close()

def insert(name,organization,phone,contact_group):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contact VALUES (NULL,?,?,?,?)",(name,organization,phone,contact_group))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="",organization="",phone="",contact_group=""):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact WHERE name=? OR organization=? OR phone=? OR contact_group=?", (name,organization,phone,contact_group))
    #cur.execute("SELECT * FROM contact WHERE name LIKE '?' OR organization LIKE '?' OR phone LIKE '?' OR contact_group LIKE '?'", (name,organization,phone,contact_group))
    #cur.execute("SELECT name, organization, phone, contact_group FROM contact WHERE name LIKE (?) OR organization LIKE (?) OR phone LIKE (?) OR contact_group LIKE (?)", ('%'+name+'%','%'+organization+'%','%'+phone+'%','%'+contact_group+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contact WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,organization,phone,contact_group):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("UPDATE contact SET name=?,organization=?,phone=?,contact_group=? WHERE id=?",(name,organization,phone,contact_group,id))
    conn.commit()
    conn.close()


connect()
