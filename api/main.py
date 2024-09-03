from django.http import JsonResponse, HttpRequest
from .models import InfoGroup, Tag
from login.models import User, AccessToken
from django.db.models import Q
from core.decorators import require_http_methods, handle_exceptions
from django.views.decorators.csrf import csrf_exempt

import base64

@require_http_methods(["POST"])
@handle_exceptions
def add(request:HttpRequest):
    token = AccessToken.objects.get(identification=request.POST["token"])
    if token is None:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )

    info_group = InfoGroup.objects.create(
        guid = request.POST["id"],
        site = base64.b64decode(request.POST["site"]),
        username = base64.b64decode(request.POST["username"]),
        password = base64.b64decode(request.POST["password"]),
        owner = token.owner,
    )

    for tag in request.POST.getlist("tags"):
        Tag.objects.create(
            content = base64.b64decode(tag),
            info_group = info_group
        )
    
    return JsonResponse(
        status=201,
        data={"message" : "ok"})

@require_http_methods(["POST"])
@handle_exceptions
def update(request:HttpRequest):
    token = AccessToken.objects.get(identification=request.POST["token"])
    if token is None:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )

    info_group = InfoGroup.objects.get(
        guid = request.POST["id"],
        owner = token.owner,
    )
    
    info_group.username = base64.b64decode(request.POST["username"])
    info_group.password = base64.b64decode(request.POST["password"])
    info_group.site = base64.b64decode(request.POST["site"])
    # info_group.tags = request.POST.getlist("tags")
    info_group.save()

    return JsonResponse(
        status=204,
        data={"message" : "ok"}
    )

@require_http_methods(["POST"])
@handle_exceptions
def delete(request:HttpRequest):
    token = AccessToken.objects.get(identification=request.POST["token"])
    if token is None:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )
    
    query = Q()
    if "ids" in request.POST:
        for i in request.POST.getlist("ids"):
            query |= Q(guid=i)
    else:
        return JsonResponse(
                status=422,
                data={"message":f"缺少参数id"}
            )

    InfoGroup.objects.filter(query).delete()

    return JsonResponse(
        status=204,
        data={"message" : "ok",}
    )

@require_http_methods(["POST"])
@handle_exceptions
def get(request:HttpRequest):
    token = AccessToken.objects.get(identification=request.POST["token"])
    if token is None:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )

    query = Q()
    if "ids" in request.POST:
        for i in request.POST["ids"]:
            query |= Q(guid = i, owner = token.owner)
    info_groups = InfoGroup.objects.filter(query)
    return JsonResponse(
        status=200,
        data={
            "message" : "ok",
            "content" : [{
                "id" : x.guid,
                "username" : base64.b64encode(x.username).decode(),
                "password" : base64.b64encode(x.password).decode(),
                "site" : base64.b64encode(x.site).decode(),
                "tags" : [base64.b64encode(tag.content).decode() for tag in Tag.objects.filter(info_group = x)],
                # "update-time" : x.update_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                # "create-time" : x.create_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            } for x in info_groups ]
    })

@require_http_methods(["POST"])
@csrf_exempt
def update_profile(request:HttpRequest):
    pic = request.POST["pic"]
    print(pic)
    print(type(pic))
    return JsonResponse(status=200, data={"message":"success"})