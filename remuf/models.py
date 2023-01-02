from django.db import models

# Create your models here.
class remuf(models.Model):
    Buku = models.CharField(max_length=100)
    Penulis = models.CharField(max_length=50)
    Penerbit = models.CharField(max_length=50)
    Jumlah = models.IntegerField(null=True)

    def __str__(self):
        return self.remuf

