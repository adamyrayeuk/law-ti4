from django.contrib import admin

from .models import Mahasiswa


class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ["nama", "npm"]
