from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response 
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class ProductAPI(APIView):
    def get(self,request,pk=None):
        print(pk)
        if pk:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request,pk=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)