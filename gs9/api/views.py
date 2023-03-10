from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg':"Hello! world"})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg':"This is post"})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method=='GET':
        return Response({'msg':"This is GET request"})

    if request.method=='POST':
        print(request.data)
        return Response({'msg':"This is post request",'data':request.data})

    if request.method=='PUT':
        # print(request.data)
        return Response({'msg':"This is put request"})