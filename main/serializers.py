from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to serialize Student to and from Json"""
    class Meta:
        model = Student
        fields = ['url', 'id', 'first_name', 'last_name',
                  'dob', 'email', 'phone_number']
        read_only_fields = ['created_on', 'modified_on']
