from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mahasiswa

@api_view(["POST"])
def update(request):
    mahasiswa = Mahasiswa.objects.create(nama=request.data.nama, npm=request.data.npm)
    mahasiswa.save()
    response = {"status": "OK"}
    return Response(response, status=status.HTTP_200_OK)