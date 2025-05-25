import sqlite3
import os

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    with open(os.path.join(os.path.dirname(__file__), '../lib/db/schema.sql'), 'r') as f:
        schema = f.read()
    try:
        cursor = conn.cursor()
        cursor.executescript(schema)
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(e)

def seed_database(conn):
    from lib.db.seed import seed_data
    seed_data(conn)

def main():
    database = "articles.db"
    conn = create_connection(database)

    if conn:
        create_tables(conn)
        seed_database(conn)
        conn.close()

if __name__ == '__main__':
    main()