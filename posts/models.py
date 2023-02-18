from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    key_words = models.CharField(max_length=255)
    is_enable = models.BooleanField(default=False)
    create_time = models.DateTimeField(default=timezone.now)
    publish_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to="files/")

    def str(self):
        return self.title
