import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(open('lib/db/schema.sql').read())
    conn.commit()
    yield
    conn.close()

def test_magazine_initialization(setup_db):
    magazine = Magazine("Tech Weekly", "Technology")
    assert magazine.name == "Tech Weekly"
    assert magazine.category == "Technology"

def test_magazine_contributors(setup_db):
    author = Author("Jane Doe")
    author.save()
    magazine = Magazine("Tech Weekly", "Technology")
    magazine.save()
    author.add_article(magazine, "Tech Trends")
    contributors = magazine.contributors()
    assert len(contributors) == 1
    assert contributors[0].name == "Jane Doe"