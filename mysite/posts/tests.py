from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class PostTest(TestCase):
    def setUp(self):

        self.post = Post.objects.create(
            user = 'test user',
            image = 'test image',
            caption = 'test caption',
            created_at = '1111-11-11 11:11',
            num_of_likes = '0',
        )
        
    def test_model(self):
        self.assertEqual(f'{self.post.user}', 'test user')
        self.assertEqual(f'{self.post.image}', 'test image')
        self.assertEqual(f'{self.post.caption}', 'test caption')
        self.assertEqual(f'{self.post.created_at}', '1111-11-11 11:11')
        self.assertEqual(f'{self.post.num_of_likes}', '0')