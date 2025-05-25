import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(open('lib/db/schema.sql').read())
    conn.commit()
    yield
    conn.close()

def test_author_initialization(setup_db):
    author = Author("Jane Doe")
    assert author.name == "Jane Doe"
    assert author.id is None

def test_author_save(setup_db):
    author = Author("Jane Doe")
    author.save()
    assert author.id is not None
    found = Author.find_by_name("Jane Doe")
    assert found.name == "Jane Doe"

def test_author_articles(setup_db):
    author = Author("Jane Doe")
    author.save()
    magazine = Magazine("Tech Weekly", "Technology")
    magazine.save()
    author.add_article(magazine, "Tech Trends")
    articles = author.articles()
    assert len(articles) == 1
    assert articles[0].title == "Tech Trends"