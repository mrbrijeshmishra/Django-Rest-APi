from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def products(request):
    data = product.objects.all()
    serializer = productSerializer(data,many=True)
    return Response({"Product":serializer.data})


@api_view(["GET"])
def single_product(request,id):
    data = product.objects.get(id=id)
    serializer = productSerializer(data)
    return Response({"Product":serializer.data})

@api_view(["POST"])
def add_prodcut(request):
    data = productSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response({"Product":data.data,"Message":"data inserted"})
    else:
        return Response({"Error":data.errors})
    

@api_view(["PUT","PATCH"])
def update_product(request,id):
    try:
        data = product.objects.get(id=id)
        serializer = productSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Data Updated Successfully","Product":serializer.data})
        else:
            return Response({"Message":serializer.data})
    except:
        return Response({"Message":"Data not Found"})
    

@api_view(["DELETE"])
def delete_product(request,id):
    try:
        data = product.objects.get(id=id)
        serializer = productSerializer(data)
        data.delete()
        return Response({"Message":"Data deleted","Product":serializer.data})
    except:
        return Response({"Error":"Record Not Found"})