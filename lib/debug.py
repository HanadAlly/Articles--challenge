# lib/debug.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def debug():
    author = Author("Jane Doe")
    author.save()
    magazine = Magazine("Tech Weekly", "Technology")
    magazine.save()
    article = author.add_article(magazine, "Tech Trends")
    print("Author Articles:", [a.title for a in author.articles()])
    print("Author Magazines:", [m.name for m in author.magazines()])
    print("Magazine Articles:", [a.title for a in magazine.articles()])
    print("Magazine Contributors:", [a.name for a in magazine.contributors()])
    print("Top Publisher:", Magazine.top_publisher().name if Magazine.top_publisher() else None)

if __name__ == "__main__":
    debug()