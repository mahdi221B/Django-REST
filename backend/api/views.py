#from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.forms.models import model_to_dict
from products.models import Products
from products.ProductSerializer import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
     instance = Products.objects.all().order_by("?").first()
     data = {}
     if (instance):
         #data = model_to_dict(instance)
         data = ProductSerializer(instance).data
         # instance -> py dict -> return JSON to my lient
     return Response(data)
