from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        conn.execute("BEGIN TRANSACTION")
        
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Doe",))
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Smith",))
        
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Monthly", "Health"))
        
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                      ("Tech Trends", 1, 1))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                      ("Health Tips", 1, 2))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ?, ?, ?)", 
                      ("AI Revolution", 2, 1))
        
        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"Error seeding data: {e}")
    finally:
        conn.close()