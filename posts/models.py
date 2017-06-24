from django.db import models

class Post(models.Model):
    content = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published', auto_now = True, null = True)

    def __str__(self):
        return self.content

class List(models.Model):
    content = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published', auto_now = True, null = True)

    def __str__(self):
        return self.content

