from django.db import models

class Hello(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    user = models.CharField(max_length=30)

    # self 자기자신을 의미
    def __str__(self):
        return self.title
        