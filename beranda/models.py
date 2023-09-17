from django.db import models

# Create your models here.

class Pengaduan(models.Model):
    nama = models.CharField(max_length=200)
    nip  = models.IntegerField()
    nik  = models.IntegerField()
    email = models.EmailField(default='.tte@deliserdangkab.go.id')
    dinas = models.CharField(max_length=400)
    nohp  = models.IntegerField()
    keluhan = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

    
