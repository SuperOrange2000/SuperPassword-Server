from django.http import JsonResponse
from .models import InfoGroup

def add(request):
    print(request.POST)
    return JsonResponse({"code":100})

