from django.http import JsonResponse, HttpRequest
from .models import InfoGroup
from login.models import User
from django.db.models import Q
import json

def add(request:HttpRequest):
    json_body = json.loads(request.body)
    InfoGroup.objects.create(
        sub_id = json_body["id"],
        user_name = json_body["username"],
        password = json_body["password"],
        tags = json_body["tags"],
        site = json_body["site"],
        owner = User.objects.first(),
    )
    return JsonResponse({
        "status" : "success",
        "message" : "ok",
    })

def update(request:HttpRequest):
    json_body = json.loads(request.body)
    info_group = InfoGroup.objects.get(
        sub_id = json_body["id"],
        owner = User.objects.first(),
    )
    if "site" in json_body.keys():
        info_group.site=json_body["site"]
    if "username" in json_body.keys():
        info_group.user_name=json_body["username"]
    if "password" in json_body.keys():
        info_group.password=json_body["password"]
    if "tags" in json_body.keys():
        info_group.tags=json_body["tags"]
    info_group.save()
    return JsonResponse({
        "status" : "success",
        "message" : "ok",
    })

def delete(request:HttpRequest):
    json_body = json.loads(request.body)
    query = Q()
    for i in json_body["ids"]:
        query |= Q(sub_id=i)
    InfoGroup.objects.filter(
        owner = User.objects.first(),
    ).filter(query).delete()
    return JsonResponse({
        "status" : "success",
        "message" : "ok",
    })

def get(request:HttpRequest):
    json_body = json.loads(request.body)
    query = Q()
    for i in json_body["ids"]:
        query |= Q(sub_id=i)
    info_groups = InfoGroup.objects.filter(
        owner = User.objects.first(),
    ).filter(query)
    return JsonResponse({
        "status" : "success",
        "message" : "ok",
        "content" : [
            {
                "id" : x.sub_id,
                "username" : x.user_name,
                "password" : x.password,
                "site" : x.site,
                "tags" : x.tags,
            } for x in info_groups
        ]
    })