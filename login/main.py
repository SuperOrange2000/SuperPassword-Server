from django.http import JsonResponse, HttpResponse
import secrets
from django.views.decorators.csrf import csrf_exempt  

# @csrf_exempt
def get_csrf_token(request):
    return HttpResponse()

def sign_up(request):
    return JsonResponse({
        "token" : secrets.token_hex(16)
    })