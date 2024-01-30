from django.http import JsonResponse, HttpRequest
from .models import InfoGroup
from login.models import User, AccessToken
from django.db.models import Q
from core.decorators import require_http_methods, handle_exceptions
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["POST"])
@handle_exceptions
def add(request:HttpRequest):
    is_success, token = AccessToken.objects.get(request.POST["token"])
    if not is_success:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )

    InfoGroup.objects.create(
        sub_id = request.POST["id"],
        user_name = request.POST["username"],
        password = request.POST["password"],
        tags = request.POST["tags"],
        site = request.POST["site"],
        owner = token.owner,
    )
    return JsonResponse(
        status=201,
        data={"message" : "ok"})

@require_http_methods(["POST"])
@handle_exceptions
def update(request:HttpRequest):
    is_success, token = AccessToken.objects.get(request.POST["token"])
    if not is_success:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )

    info_group = InfoGroup.objects.get(
        sub_id = request.POST["id"],
        owner = token.owner,
    )
    if "site" in request.POST.keys():
        info_group.site=request.POST["site"]
    if "username" in request.POST.keys():
        info_group.user_name=request.POST["username"]
    if "password" in request.POST.keys():
        info_group.password=request.POST["password"]
    if "tags" in request.POST.keys():
        info_group.tags=request.POST["tags"]
    info_group.save()
    return JsonResponse(
        status=204,
        data={"message" : "ok"}
    )

@require_http_methods(["POST"])
@handle_exceptions
def delete(request:HttpRequest):
    is_success, token = AccessToken.objects.get(request.POST["token"])
    if not is_success:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )
    
    query = Q()
    if "ids" in request.POST:
        if isinstance(request.POST["ids"], str):
            query |= Q(sub_id=request.POST["ids"])
        else:
            for i in request.POST["ids"]:
                query |= Q(sub_id=i)
    InfoGroup.objects.filter(
        owner = token.owner,
    ).filter(query).delete()
    return JsonResponse(
        status=204,
        data={"message" : "ok",}
    )

@require_http_methods(["POST"])
@handle_exceptions
def quick_get(request:HttpRequest):
    is_success, token = AccessToken.objects.get(request.POST["token"])
    if not is_success:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )

    query = Q()
    if "ids" in request.POST:
        for i in request.POST["ids"]:
            query |= Q(sub_id=i)
    info_groups = InfoGroup.objects.filter(
        owner = token.owner,
    ).filter(query)
    return JsonResponse(
        status=200,
        data={
            "message" : "ok",
            "content" : [{
                "id" : x.sub_id,
                "site" : x.site,
                "tags" : x.tags,
            } for x in info_groups ]
    })

@require_http_methods(["POST"])
@handle_exceptions
def get(request:HttpRequest):
    is_success, token = AccessToken.objects.get(request.POST["token"])
    if not is_success:
        return JsonResponse(
            status=401,
            data={"message" : "会话过期"}
        )

    info_group = InfoGroup.objects.filter(owner = token.owner).get(id=request.POST["id"])
    return JsonResponse(
        status=200,
        data={
            "message" : "ok",
            "content" : {
                "id" : info_group.sub_id,
                "username" : info_group.user_name,
                "password" : info_group.password,
                "site" : info_group.site,
                "tags" : info_group.tags,
    }})

@require_http_methods(["POST"])
@csrf_exempt
def update_profile(request:HttpRequest):
    pic = request.POST["pic"]
    print(pic)
    print(type(pic))
    return JsonResponse(status=200, data={"message":"success"})