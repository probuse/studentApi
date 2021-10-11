from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows students to be viewed and edited"""
    queryset = Student.objects.all().order_by('-modified_on')
    serializer_class = StudentSerializer
