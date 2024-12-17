class Article:
    all = []
    
    def __repr__(self):
        return f"<Article title: {self.title}, author: {self.author.name}, magazine: {self.magazine.name}>"
    
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.__class__.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if type(value) == Author:
            self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,value):
        if type(value) == Magazine:
            self._magazine = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self,"title"):
            self._title = value

        
class Author:
    def __repr__(self):
        return f"<Author name: {self.name}>"
    
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value, str) and len(value) >= 0 and not hasattr(self,"name"):
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return [magazine.category for magazine in self.magazines()] or None


class Magazine:

    @classmethod
    def top_publisher(cls):
        count = {}
        for article in Article.all:
            magazine = article.magazine
            count[magazine] = count.get(magazine,0) + 1
        return None if not count else max(count, key=count.get)

    def __repr__(self):
        return f"<Magazine name: {self.name}, category: {self.category}>"

    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        count = {}
        for article in self.articles():
            author = article.author
            count[author] = count.get(author,0) + 1
        return [key for key,val in count.items() if val > 1] or None