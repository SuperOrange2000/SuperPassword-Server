from django.http import JsonResponse, HttpRequest
from .models import InfoGroup
from login.models import User, UserLoginToken
from django.db.models import Q
from core.decorators import require_http_methods, handle_exceptions

def get_token(identification):
    try:
        token = UserLoginToken.objects.get(identification=identification)
    except UserLoginToken.DoesNotExist:
        return dict(
            status=401,
            data={"message" : "未知token"}
        )
    except UserLoginToken.TokenTimeoutError:
        return dict(
            status=401,
            data={"message" : "会话过期"}
        )
    finally:
        return token

@require_http_methods(["POST"])
@handle_exceptions
def add(request:HttpRequest):
    token = get_token(request.POST["token"])
    if isinstance(token, dict):
        return JsonResponse(**token)

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
    token = get_token(request.POST["token"])
    if isinstance(token, dict):
        return JsonResponse(**token)

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
    token = get_token(request.POST["token"])
    if isinstance(token, dict):
        return JsonResponse(**token)
    
    query = Q()
    if "ids" in request.POST:
        for i in request.POST["ids"]:
            query |= Q(sub_id=i)
    InfoGroup.objects.filter(
        owner = token.owner,
    ).filter(query).delete()
    return JsonResponse(
        status=204,
        data={"message" : "ok",}
    )

@require_http_methods(["GET"])
@handle_exceptions
def basic_get(request:HttpRequest):
    token = get_token(request.GET["token"])
    if isinstance(token, dict):
        return JsonResponse(**token)

    query = Q()
    if "ids" in request.GET:
        for i in request.GET["ids"]:
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

@require_http_methods(["GET"])
@handle_exceptions
def detailed_get(request:HttpRequest):
    token = get_token(request.GET["token"])
    if isinstance(token, dict):
        return JsonResponse(**token)

    info_group = InfoGroup.objects.filter(owner = token.owner).get(id=request.GET["id"])
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