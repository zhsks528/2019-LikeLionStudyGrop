from django.db import models

class Book(models.Model):
    
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('book_deit', kwargs={'pk' : self.pk})