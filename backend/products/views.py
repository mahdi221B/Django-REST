from rest_framework import generics
from .models import Products
from .ProductSerializer import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all() #specifies the queryset of "Products" objects that should be returned
    serializer_class = ProductSerializer #indicates the serializer to use for the model.
    # lookup_field='pk'  ==  instance=Products.objects.get(pk=1)
    # def perform_create(self, serializer):
    #    print(serializer.validated_data) 
    #    print(serializer.validated_data.get('title'))
        
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # def perform_create(self, serializer):
    #     serializer.save(user= self.request.user)
    



#Product_List_Create = ProductListCreateAPIView.as_view()
#Product_Retrieve_Update_Destroy = ProductListCreateAPIView.as_view()