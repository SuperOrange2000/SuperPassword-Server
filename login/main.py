from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import *
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from core.decorators import require_http_methods, handle_exceptions

@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse()

@require_http_methods(["POST"])
@handle_exceptions
def sign_up(request:HttpRequest):
    if User.objects.filter(username = request.POST["username"]).exists():
        return JsonResponse(
            status = 409,
            data={
            "message" : "该用户名已被注册",
        })
    
    u = User.objects.create(
        username = request.POST["username"],
    )
    aes_key = hashlib.sha256((u.salt + request.POST["password"]).encode()).digest()
    encryptor = Cipher(algorithms.AES(aes_key), modes.CBC(u.iv)).encryptor()
    u.check_code = encryptor.update(b'\x10'*algorithms.AES.block_size)+encryptor.finalize()
    if "nickname" in request.POST.keys():
        u.nickname = request.POST["nickname"]

    token = AccessToken.objects.create(owner=u).identification
    u.save()

    return JsonResponse(
        status=201,
        data={
        "message" : "ok",
        "content" : token
    })

@require_http_methods(["POST"])
@handle_exceptions
def login(request:HttpRequest):
    if not User.objects.filter(username = request.POST["username"]).exists():
        return JsonResponse(
            status = 404,
            data={
            "message" : "用户未注册",
        })
    u = User.objects.get(
        username = request.POST["username"]
    )
    aes_key = hashlib.sha256((u.salt + request.POST["password"]).encode()).digest()
    decryptor = Cipher(algorithms.AES(aes_key), modes.CBC(u.iv)).decryptor()

    if b'\x10'*algorithms.AES.block_size == decryptor.update(u.check_code) + decryptor.finalize():
        query_set = AccessToken.objects.filter(owner=u, device=request.POST["device"])
        if query_set.exists() and AccessToken.objects.check_timeout(query_set.first()):
            identification_code = query_set.first().identification
        else:
            identification_code = AccessToken.objects.create(owner=u).identification
        return JsonResponse(
            status=200,
            data={
            "message" : "ok",
            "content" : identification_code
        })
    else:
        return JsonResponse(
            status=401,
            data={
                "message" : "密码错误"
        })
