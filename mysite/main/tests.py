from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileTest(TestCase):
    def setUp(self):
        
        self.user = get_user_model().objects.create_user(
            username = 'shahab',
            password = '1234'
            )
        
        self.profile = Profile.objects.create(
            user = self.user,
            id_user = '1',
            first_name = 'test first_name',
            last_name = 'test last_name',
            bio = 'test bio',
            profileimg = 'test profileimg',
            location = 'test location',
        )
        
    def test_model(self):
        self.assertEqual(f'{self.profile.user}', 'shahab')
        self.assertEqual(f'{self.profile.id_user}', '1')
        self.assertEqual(f'{self.profile.first_name}', 'test first_name')
        self.assertEqual(f'{self.profile.last_name}', 'test last_name')
        self.assertEqual(f'{self.profile.profileimg}', 'test profileimg')
        self.assertEqual(f'{self.profile.location}', 'test location')
