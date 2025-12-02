from django.shortcuts import render, Response
from rest_framework.decorators import api_view
from models import Product
from serializers import ProductSerializer

# Create your views here.

@api_View(['GET'])
def product_List(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

@api_View(['GET'])
def product_Detail(request):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def add_Product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_Valid():
        serializer.save()
        return Response(serializer.data)