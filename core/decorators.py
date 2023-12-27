from functools import wraps
from django.http import HttpRequest, JsonResponse

def require_http_methods(methods):
    def decorator(func):
        @wraps(func)
        def wrapper(request:HttpRequest):
            if request.method not in methods:
                return JsonResponse(
                    status=405,
                    data={"message":"非法方法"}
                )
            return func(request)
        return wrapper
    return decorator

def check_keys(func):
    @wraps(func)
    def wrapper(request:HttpRequest):
        try:
            return func(request)
        except KeyError as e:
            return JsonResponse(
                status=422,
                data={"message":f"缺少参数{e}"}
            )
    return wrapper