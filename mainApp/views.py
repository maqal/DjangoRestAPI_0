from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .appSerializers import * 
from rest_framework.response import Response

# Create your views here and crud

class StudentView(APIView):
    def get(self, request, id = None):
        if id:
            item = models.Student.objects.get(id = id)
            serializer = StudentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status = Response.status_code)
        
        items = Student.objects.all()
        serializer = StudentSerializer(items, many = True)
        return Response({"status": "success", "data": serializer.data}, status = Response.status_code)

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if(serializer.is_valid(raise_exception = True)):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"status": "error", "data": serializer.errors}, status = Response.status_text)

    def patch(self, request, id = None):
        item = Student.objects.get(id = id)
        serializer = StudentSerializer(item, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status = Response.status_code)
        else:
            return Response({"status": "error", "data": serializer.errors}, status = Response.status_text)

    def delete(self, request, id = None):
        item = Student.objects.filter(id = id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
