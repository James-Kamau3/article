class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []
        
    def name(self):
        return self.name
    
    def articles(self):
        return self.articles
    

author = Author("James Kamau")
articles = Author("THINK BIG")

print(author.name)
print(articles.name)
