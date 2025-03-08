from django.http import JsonResponse
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all().values()  # Devuelve todos los productos
    return JsonResponse({"productos": list(productos)})
