import pytest
from lib.models.article import Article
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

def test_article_initialization(setup_db):
    author = Author("Jane Doe")
    author.save()
    magazine = Magazine("Tech Weekly", "Technology")
    magazine.save()
    article = Article("Tech Trends", author.id, magazine.id)
    assert article.title == "Tech Trends"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id

def test_article_save(setup_db):
    author = Author("Jane Doe")
    author.save()
    magazine = Magazine("Tech Weekly", "Technology")
    magazine.save()
    article = Article("Tech Trends", author.id, magazine.id)
    article.save()
    assert article.id is not None
    found = Article.find_by_id(article.id)
    assert found.title == "Tech Trends"