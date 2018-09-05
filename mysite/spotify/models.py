from django.db import models

class Token(models.Model):
    key = models.URLField(max_length = 500)