from functools import wraps
from django.http import HttpRequest, JsonResponse
from typing import List, Literal

def require_http_methods(methods:List[Literal["GET", "POST", "PUT", "DELETE"]]):
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

def handle_exceptions(func):
    @wraps(func)
    def wrapper(request:HttpRequest):
        try:
            return func(request)
        except KeyError as e:
            return JsonResponse(
                status=422,
                data={"message":f"缺少参数{e}"}
            )
        except Exception as e:
            print(f"Exception {e} occurred in {func.__name__}")
            return JsonResponse(
                status=500,
                data={"message":"服务器未知错误"}
            )
    return wrapper