import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("bbc-news", "BBC")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))