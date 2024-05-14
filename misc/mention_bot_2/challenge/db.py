import sqlite3
from telegram import Update
from string import ascii_letters, digits
from random import choice


blacklist = ["delete", "drop", "update", "insert", "alter", "upsert", "truncate", "create"]

conn = None



def gen_random_string(n):
    return ''.join(choice(ascii_letters) for i in range(n))

USERNAME = gen_random_string(30)

def init_db():
    global conn
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    # Create a table to store user IDs
    # Usernames
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS allowed_users (
            user_id INTEGER PRIMARY KEY,
            chat_id INTEGER,
            username TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY,
            quote TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS private_users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );
    ''')

    quotes_data = [
    ("What is the music of life?, Silence, my brother.",),
    ("What is the color of night?, Sanguine, my brother.",),
    ("What is life's greatest illusion?, Innocence, my brother.",),
    ("What is the flavor of fear?, Sublime, my Brother.",),
    ("What is the gift of death?, Solace, my Brother.",)
    ]

    cursor.executemany("INSERT INTO quotes (quote) VALUES (?)", quotes_data)
    # initialize the quotes table with some quotes

    #insert a flag
    cursor.execute(f"INSERT INTO private_users (user_id, username, password) VALUES (1, '{USERNAME}', '{'ingeneer{s3cur3_p45s}'}')")

    conn.commit()

    return conn


def get_all_users(chat_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM allowed_users WHERE chat_id = ?', (chat_id,))
    return cursor.fetchall()

def get_all_users_in_group(update: Update):
    chat_id = update.message.chat_id
    users = get_all_users(chat_id)
    return users

def get_all_quotes():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quotes')
    return cursor.fetchall()

def get_quote_by_id(quote_id):
    cursor = conn.cursor()
    for i in quote_id.split(' '):
        if i.lower() in blacklist:
            raise Exception("nope")
    query = "SELECT * FROM quotes WHERE id=?"
    print(f"query: {query}")
    cursor.execute(query, (quote_id,))
    out = cursor.fetchone()
    print(f"fetched: {out}")
    return out