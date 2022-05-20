class Post:

    all_posts = []

    def __init__(self,author,category,content):
        self.author = author
        self.category = category
        self.content = content
      


    def save_posts(self):
        Post.all_posts.append(self)


    @classmethod
    def clear_posts(cls):
        Post.all_posts.clear()