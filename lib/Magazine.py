class Magazine:
    
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all_magazines.append(self)

    def name(self):
        return self.name
    
    def category(self):
        return self.category
    
    @classmethod
    def all(cls):
        return cls.all_magazines
    
# Create magazine instances
magazine1 = Magazine("Magazine A", "Category A")
magazine2 = Magazine("Magazine B", "Category B")
magazine3 = Magazine("Magazine C", "Category C")

for magazine in Magazine.all():
    print(magazine.name, magazine.category) 
