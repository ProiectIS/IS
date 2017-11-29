from __future__ import unicode_literals

from django.db import models

class Mainpage(models.Model):
    author=models.CharField(max_length=30)

    def __str__(self):
        return self.author
