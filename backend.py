import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # id is the serial number for books, it uniquely identifies each book
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # NULL is for id Python automatically creates id
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows


# We pass empty strings bc, if the user only enters one parameter we get an error
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# Deleting the entire tuple


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # NULL is for id Python automatically creates id
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # NULL is for id Python automatically creates id
    cur.execute("UPDATE books SET title=?,author=?,year=?,isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


# Function Calls
connect()
# # insert("Godfather", "Mario Puzo", 1950, 9471)
# # insert("Da Vinci Code", "Dan Brown", 2005, 9898)

# # delete(3)
# # print(search(isbn="Dan Brown"))
# update(2, "The Shining", "Stephen King", 1972, 7845)
# print(view())
