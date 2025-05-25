from lib.db.connection import get_connection
from lib.db.seed import seed_data

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    with open('lib/db/schema.sql', 'r') as f:
        schema = f.read()
    cursor.executescript(schema)
    conn.commit()
    
    seed_data()
    
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()