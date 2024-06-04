
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.append(self)
    #this method is a getter for the title attribute
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
         if isinstance(title, str):
            self._title = title
        
     

class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name

    def articles(self):
        return [articles for articles in Article.all if articles.author == self]

    # Method to get all unique magazines the author has contributed to
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    # Method to add a new article for the author
    def add_article(self, magazine, title):
        articles = Article(self, magazine, title)
        return articles
   

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

   

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
   
    @category.setter
    def category(self, new_category):
      if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
    
    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None
   
    def contributing_authors(self):
     #initialise an empty dictionary
      authors = {}
      # iterate over articles of teh current magazine
      for article in self.articles():
          #check if the author is already in the dictionary
          if article.author in authors:

              authors[article.author] += 1
          else:
              authors[article.author] = 1

      contributing_authors = [author for author, count in authors.items() if count >= 2]
      return contributing_authors if contributing_authors else None
    
   
    @staticmethod
    def top_publisher():

        if Article.all:

            magazine_article_count = {}
            # iterate over articles
            for article in Article.all:

                magazine = article.magazine
                #check if the magazine is already in the dictionary
                if magazine in magazine_article_count:

                    magazine_article_count[magazine] += 1
                else:
                   magazine_article_count[magazine] = 1

            return max(magazine_article_count, key=magazine_article_count.get)
        return None

    
author1 = Author("Brian Maitho")
author2 = Author("Tulley Mutea")
author3 = Author("Ted Kiplagat")


magazine1 = Magazine("Forbes", "Science")
magazine2 = Magazine("Todays Tech", "Technology")


author1.add_article(magazine1, "The Latest Discoveries in Physics")
author1.add_article(magazine2, "Advancements in Cancer Treatment")
author2.add_article(magazine1, "The Future of Deep sea Exploration")
author3.add_article(magazine1, "Understanding Mechanics")
author3.add_article(magazine2, "The Rise of Cybercrime")

author1.add_article(magazine1, "New Developments in Tech")
author2.add_article(magazine1, "Exploring Oceans: Recent Findings")

contributing_authors = magazine1.contributing_authors()

if contributing_authors:
    print("Authors who have written more than two articles for Magazine one:")
    for author in contributing_authors:
        print(author.name)

top_publisher = Magazine.top_publisher()

if top_publisher:
   
    print(f"Category: {top_publisher.category}")
else:
    print("No articles found.")