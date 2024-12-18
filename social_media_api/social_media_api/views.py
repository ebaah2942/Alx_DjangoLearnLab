from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "posts": "/posts/",
        "users": "/users/",
        "comments": "/comments/",
        "status": "OK"
    })
