from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mahasiswa

from django.db import DataError

import json

@api_view(["POST"])
def update(request):
    try:
        data = json.loads(request.data.get("_content"))
        mahasiswa = mahasiswa.objects.get(npm=data['npm'])
        mahasiswa.nama = data['nama']
        response = {"status": "OK"}
        return Response(response, status=status.HTTP_200_OK)
    except Mahasiswa.DoesNotExist:
        mahasiswa = Mahasiswa.objects.create(nama=data['nama'], npm=data['npm'])
        mahasiswa.save()
        response = {"status": "OK"}
        return Response(response, status=status.HTTP_201_CREATED)
    except KeyError:
        response = {"status": "Bad Request", "message": "Pastikan payload berisi nama dan NPM"}
    except DataError:
        response = {"status": "Bad Request", "message": "pastikan NPM berisi maksimal 10 karakter"}