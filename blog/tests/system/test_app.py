from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):

    def setUp(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {'Test': blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test create blog', 'Test author', 'q')

                app.menu()

                mocked_ask_create_blog.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()

            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.menu') as mocked_print_blogs:
            with patch('builtins.input', return_value='l'):
                app.menu()

                mocked_print_blogs.assert_called_with()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()

            mocked_print.assert_called_with('- Test by Test author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test author')  # mocking in ask_create_blog title and author,
            # can be more arguments, depends on how many inputs in function
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def ask_read_blog(self):


        with patch('builtins.input', return_value='Test') as mocked_input:  # programmed return value
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

        mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test post', 'Test content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

        mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
    ---Post title---
    
    Post content
    
    '''

        with patch('builtins.print') as mocked_print:
            app.print_post(post)

        mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test title', 'Test content')

            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test content')
