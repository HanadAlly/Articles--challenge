from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.execute("BEGIN TRANSACTION")
        # Insert authors
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Doe",))
        author1_id = cursor.lastrowid
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Smith",))
        author2_id = cursor.lastrowid
        # Insert magazines
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
        magazine1_id = cursor.lastrowid
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Monthly", "Health"))
        magazine2_id = cursor.lastrowid
        # Insert articles
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                      ("Tech Trends", author1_id, magazine1_id))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                      ("Health Tips", author1_id, magazine2_id))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                      ("AI Revolution", author2_id, magazine1_id))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                      ("Tech Future", author2_id, magazine1_id))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                      ("Tech Now", author2_id, magazine1_id))
        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"Error seeding data: {e}")
    finally:
        conn.close()