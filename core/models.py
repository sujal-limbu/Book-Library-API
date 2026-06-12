from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    published_year = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name