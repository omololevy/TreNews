import unittest
from app.models import NewsArticle

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticle class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = NewsArticle("CNN", "John Doe", "Christmas in the City", "/home", "/image", "01-01-2023", "Oh", "Boy")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,NewsArticle))