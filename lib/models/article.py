from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self._title = None
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Title must be a non-empty string")
        self._title = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            conn.execute("BEGIN TRANSACTION")
            if self.id is None:
                cursor.execute(
                    "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) RETURNING id",
                    (self.title, self.author_id, self.magazine_id)
                )
                self.id = cursor.fetchone()['id']
            else:
                cursor.execute(
                    "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                    (self.title, self.author_id, self.magazine_id, self.id)
                )
            conn.execute("COMMIT")
        except Exception as e:
            conn.execute("ROLLBACK")
            raise Exception(f"Error saving article: {e}")
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['title'], row['author_id'], row['magazine_id'], row['id']) if row else None

    def author(self):
        from lib.models.author import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (self.author_id,))
        row = cursor.fetchone()
        conn.close()
        return Author(row['name'], row['id']) if row else None

    def magazine(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine_id,))
        row = cursor.fetchone()
        conn.close()
        return Magazine(row['name'], row['category'], row['id']) if row else None