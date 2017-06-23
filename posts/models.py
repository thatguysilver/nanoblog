from django.db import models

class Post(models.Model):
    content = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published', null = True)

    def __str__(self):
        return self.content
