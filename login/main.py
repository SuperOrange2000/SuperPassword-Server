from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .models import *
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse()

def sign_up(request:HttpRequest):
    json_body = json.loads(request.body)

    if User.objects.filter(username = json_body["username"]).exists():
        return HttpResponse(
            status = 409,
            content={
            "message" : "该用户名已被注册",
        })
    
    u = User.objects.create(
        username = json_body["username"],
    )
    aes_key = hashlib.sha256((u.solt + json_body["password"]).encode()).hexdigest()
    encryptor = Cipher(algorithms.AES(aes_key), modes.CBC(u.iv)).encryptor()
    u.check_code = encryptor.update(b'\x10'*algorithms.AES.block_size)+encryptor.finalize()
    if "nickname" in json_body.keys():
        u.nickname = json_body["nickname"]

    token = UserLoginToken.objects.create(owner=u).identification
    u.save()

    return HttpResponse(
        status=200,
        content={
        "message" : "ok",
        "content" : token
    })

def login(request:HttpRequest):
    json_body = json.loads(request.body)
    u = User.objects.get(
        username = json_body["username"]
    )
    aes_key = hashlib.sha256((u.solt + json_body["password"]).encode()).hexdigest()
    decryptor = Cipher(algorithms.AES(aes_key), modes.CBC(u.iv)).decryptor()

    if '\x10'*algorithms.AES.block_size == decryptor.update(u.check_code) + decryptor.finalize():
        query_set = UserLoginToken.objects.filter(owner=u, device=json_body["device"])
        if query_set.exists():
            token = query_set.first().identification
        else:
            token = UserLoginToken.objects.create(owner=u).identification
        return HttpResponse(
            status=200,
            content={
            "message" : "ok",
            "content" : token
        })
    else:
        return HttpResponse(
            status=401,
            content={
                "message" : "密码错误"
            }
        )