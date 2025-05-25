import unittest
from lib.models.article import Article

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.article = Article(title="Sample Article", content="This is a sample article.", author_id=1)

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Sample Article")
        self.assertEqual(self.article.content, "This is a sample article.")
        self.assertEqual(self.article.author_id, 1)

    def test_article_string_representation(self):
        self.assertEqual(str(self.article), "Sample Article")

if __name__ == '__main__':
    unittest.main()