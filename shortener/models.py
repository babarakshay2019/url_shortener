from django.db import models
from django.utils.crypto import get_random_string


class URLMapping(models.Model):
    short_code = models.CharField(max_length=10, unique=True, db_index=True, default=get_random_string(6))
    long_url = models.URLField()
    visit_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.short_code}"