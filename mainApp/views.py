from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .appSerializers import * 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here and crud

class TeacherList(APIView):
    
    '''
        Get
    '''
    def get(self, request, format = None):
        teachersList = Teacher.objects.all()
        teacherSerializer = TeacherSerializer(teachersList, many = True)
        return Response(teacherSerializer.data)
    
    
    '''
        Create
    '''
    def post(self, request, format = None):
        teacherSerializer = TeacherSerializer(data = request.data)
        if teacherSerializer.is_valid():
            teacherSerializer.save()
            return Response(teacherSerializer.data, status = status.HTTP_201_CREATED)
        return Response(teacherSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class TeacherDetails(APIView):
    
    '''
        Retrieve
    '''
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk = pk)
        except Teacher.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        teacher = self.get_object(pk)
        teacherSerializer = TeacherSerializer(teacher)
        return Response(teacherSerializer.data)
    
    '''
        Update
    '''
    def put(self, request, pk, format = None):
        teacher = self.get_object(pk)
        teacherSerializer = TeacherSerializer(teacher, data = request.data)
        if(teacherSerializer.is_valid()):
            teacherSerializer.save()
            return Response(teacherSerializer.data)
        return Response(teacherSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    '''
        Delete
    '''
    def delete(self, request, pk, format = None):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class StudentView(APIView):
    def get(self, request, id = None):
        if id:
            item = Student.objects.get(id = id)
            serializer = StudentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status = status.HTTP_200_OK)
        
        items = Student.objects.all()
        serializer = StudentSerializer(items, many = True)
        return Response({"status": "success", "data": serializer.data}, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if(serializer.is_valid(raise_exception = True)):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

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
