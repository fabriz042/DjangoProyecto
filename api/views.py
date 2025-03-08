from django.http import JsonResponse

def simple_api(request):
    data = {"mensaje": "Hola, esta es una API simple"}
    return JsonResponse(data)
