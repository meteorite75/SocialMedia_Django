from django.db import models
import uuid
from datetime import datetime

class Post(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_image')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    num_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.caption