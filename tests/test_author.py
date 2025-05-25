import unittest
from lib.models.author import Author

class TestAuthor(unittest.TestCase):

    def setUp(self):
        self.author = Author(name="John Doe", bio="An aspiring writer.")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "John Doe")
        self.assertEqual(self.author.bio, "An aspiring writer.")

    def test_author_repr(self):
        self.assertEqual(repr(self.author), "Author(name='John Doe', bio='An aspiring writer.')")

if __name__ == '__main__':
    unittest.main()