from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name', 'regNo', 'mobile']
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
       model = Teacher
       fields = '__all__'