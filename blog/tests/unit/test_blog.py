from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test author')
        b2 = Blog('My day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My day by Rolf (0 posts)')

    def test_repr_multiple(self):
        b = Blog('Test', 'Test author')
        b.posts = ['Test']

        b2 = Blog('My day', 'Rolf')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test author (1 post)')
        self.assertEqual(b2.__repr__(), 'My day by Rolf (2 posts)')
