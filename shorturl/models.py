from django.db import models
import string, random

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) #unique and random genrated

class ShortURL(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)
