from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=255)
    npm = models.CharField(max_length=10)