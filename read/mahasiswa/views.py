from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mahasiswa

import json

@api_view(["GET"])
def read(request, id):
    try:
        mahasiswa = Mahasiswa.objects.get(npm=id)
        response = {
            "status": "OK",
            "npm": mahasiswa.npm,
            "nama": mahasiswa.nama,
        }
        return Response(response, status=status.HTTP_200_OK)
    except Mahasiswa.DoesNotExist():
        return Response({"status":"Bad Request", "message":"NPM tidak dapat ditemukan"}, status=status.HTTP_400_BAD_REQUEST)