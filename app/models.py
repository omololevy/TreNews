class NewsArticle:
    def __init__(self, source_name, author, title, url, url_to_image, published_at, description, content):
        self.source_name=source_name
        self.author=author
        self.title=title
        self.url=url
        self.url_to_image=url_to_image
        self.published_at=published_at
        self.description=description
        self.content=content

class Sources:
    def __init__(self, source_id, source_name):
        self.source_id=source_id
        self.source_name=source_name