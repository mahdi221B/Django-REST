from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products
from products.ProductSerializer import ProductSerializer

@api_view(["GET"])
def get_random_product(request, *args, **kwargs):
     instance = Products.objects.all().order_by("?").first()
     #instance = Products.objects.get(pk=1)
     data = {}
     if (instance):
         #data = model_to_dict(instance)
         data = ProductSerializer(instance).data
         # instance -> py dict -> return JSON to my lient
     return Response(data)
 

@api_view(["POST"])
def add_product(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(serializer.data)
        print(instance)
        return Response(serializer.data, status=201)  # Return a 201 Created status code
    else:
        return Response(serializer.errors, status=400)  # Return a 400 Bad Request status code with serializer errors