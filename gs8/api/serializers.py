from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #validators
    def start_with_r(value):
        if value[0].lower()!='r':
            raise serializers.ValidationError("name should be start with r")
        return value

    name=serializers.CharField(validators=[start_with_r])
    
    class Meta:
        model=Student
        fields=['name','roll','city']

    # def validate_roll(self, value):
    #     if value >=200:
    #         raise serializers.ValidationError("Seats are full")
    #     else:
    #         return value

    # object level validation
    # def validate(self, data):
    #     nm=data.get('name')
    #     ct=data.get('city')

    #     if nm.lower()=='Aditya' and ct.lower()!= 'Delhi':
    #         raise serializers.ValidationError("City should be Hissar")
    #     return data

    

       
    
   
