from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=255)
    npm = models.CharFIeld(max_length=10)