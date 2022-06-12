from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mahasiswa

import json

@api_view(["POST"])
def update(request):
    data = json.loads(request.data.get("_content"))
    mahasiswa = Mahasiswa.objects.create(nama=data['nama'], npm=data['npm'])
    mahasiswa.save()
    response = {"status": "OK"}
    return Response(response, status=status.HTTP_200_OK)