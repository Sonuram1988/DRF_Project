from rest_framework import serializers
from django import forms

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=30)
    id=serializers.IntegerField()

# class StudentForm(forms.Form):
#     name=forms.CharField(max_length=30)
#     roll=forms.IntegerField()
#     city=forms.CharField(max_length=30)
