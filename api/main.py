from django.http import JsonResponse, HttpRequest
from .models import InfoGroup, UserEntityRelation
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
        username = base64.b64decode(request.POST["username"]),
        password = base64.b64decode(request.POST["password"]),
        site = base64.b64decode(request.POST["site"]),
        tags = base64.b64decode(request.POST["tags"]),
        # extra_info = base64.b64decode(request.POST["extra_info"]),
        salt = base64.b64decode(request.POST["salt"]),
    )

    UserEntityRelation.objects.create(
        personal_info_id = request.POST["id"],
        info_group = info_group,
        owner = token.owner,
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

    info_group = UserEntityRelation.objects.get(
        personal_info_id = request.POST["id"],
        owner = token.owner,
    ).info_group
    
    info_group.username = base64.b64decode(request.POST["username"])
    info_group.password = base64.b64decode(request.POST["password"])
    info_group.site = base64.b64decode(request.POST["site"])
    info_group.tags = base64.b64decode(request.POST["tags"])
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
        if isinstance(request.POST["ids"], str):
            query |= Q(personal_info_id=request.POST["ids"])
        else:
            for i in request.POST["ids"]:
                query |= Q(personal_info_id=i)

    info_group_ids = UserEntityRelation.objects.filter(
        owner = token.owner,
    ).filter(query).values_list("info_group", flat=True)

    query = Q()
    for i in info_group_ids:
        query |= Q(id=i)
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
            query |= Q(personal_info_id=i)
    info_group_relations = UserEntityRelation.objects.filter(
        owner = token.owner,
    ).filter(query)
    return JsonResponse(
        status=200,
        data={
            "message" : "ok",
            "content" : [{
                "id" : x.personal_info_id,
                "username" : base64.b64encode(x.info_group.username).decode(),
                "password" : base64.b64encode(x.info_group.password).decode(),
                "site" : base64.b64encode(x.info_group.site).decode(),
                "tags" : base64.b64encode(x.info_group.tags).decode(),
                "salt" : base64.b64encode(x.info_group.salt).decode(),
                "update-time" : x.info_group.update_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "create-time" : x.info_group.create_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            } for x in info_group_relations ]
    })

@require_http_methods(["POST"])
@csrf_exempt
def update_profile(request:HttpRequest):
    pic = request.POST["pic"]
    print(pic)
    print(type(pic))
    return JsonResponse(status=200, data={"message":"success"})