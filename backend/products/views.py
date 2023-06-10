from rest_framework import generics, mixins
from .models import Products
from .ProductSerializer import ProductSerializer

#1 View per action
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        # send a Django signal
product_list_create_view = ProductListCreateAPIView.as_view()




class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    def perform_update(self, serializer):
            instance = serializer.save()
            if not instance.content:
                instance.content = instance.title
product_update_view = ProductUpdateAPIView.as_view()




class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
product_detail_view = ProductDetailAPIView.as_view()



#2 mixin
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)
product_destroy_view = ProductDestroyAPIView.as_view()



class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs): #HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)
    
    
    
    
#3 Using just two Views
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Products.objects.all() #specifies the queryset of "Products" objects that should be returned
#     serializer_class = ProductSerializer #indicates the serializer to use for the model.
#     lookup_field='pk' #==instance=Products.objects.get(pk=1)
#     def perform_create(self, serializer):
#         print(serializer.validated_data) 
#         print(serializer.validated_data.get('title'))
        
# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     # def perform_create(self, serializer):
#     #     serializer.save(user= self.request.user)