from django.db import models
from uuid import uuid4

class books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year= models.IntegerField(max_length=4)
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    