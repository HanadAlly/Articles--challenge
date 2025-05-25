from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def main():
    author = Author("Jane Doe")
    author.save()
    magazine = Magazine("Tech Weekly", "Technology")
    magazine.save()
    article = author.add_article(magazine, "Tech Trends")
    
    print("Author Articles:", [a.title for a in author.articles()])
    print("Author Magazines:", [m.name for m in author.magazines()])
    print("Magazine Articles:", [a.title for a in magazine.articles()])
    print("Magazine Contributors:", [a.name for a in magazine.contributors()])

if __name__ == "__main__":
    main()