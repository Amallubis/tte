from django.db import models

# Create your models here.

class Berita(models.Model):
    fotos = models.ImageField(upload_to='foto/')
    judul = models.CharField(max_length=200)
    postingan= models.TextField()
    publish  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    