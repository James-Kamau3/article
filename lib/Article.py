class Article:

    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all_articles.append(self)

    def title (self):
        return self.title
    
    @classmethod
    def all(cls):
        return cls.all_articles
    
    def author (self):
        return self.author
    
    def magazine (self):
        return self.magazine
    

#creating instances of articles
article1 = Article("Author A", "Magazine A", "Title A")
article2 = Article("Author B", "Magazine B", "Title B")
article3 = Article("Author C", "Magazine C", "Title C")


for article in Article.all():
    print (article.author, article.magazine, article.title)