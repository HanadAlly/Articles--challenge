import unittest
from lib.models.magazine import Magazine

class TestMagazine(unittest.TestCase):

    def setUp(self):
        self.magazine = Magazine(title="Tech Today", issue_number=42)

    def test_magazine_creation(self):
        self.assertEqual(self.magazine.title, "Tech Today")
        self.assertEqual(self.magazine.issue_number, 42)

    def test_magazine_title(self):
        self.magazine.title = "Science Monthly"
        self.assertEqual(self.magazine.title, "Science Monthly")

    def test_magazine_issue_number(self):
        self.magazine.issue_number = 43
        self.assertEqual(self.magazine.issue_number, 43)

if __name__ == '__main__':
    unittest.main()