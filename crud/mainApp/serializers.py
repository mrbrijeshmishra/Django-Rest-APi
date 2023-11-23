from rest_framework import serializers
from .models import student

class Student(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self,validated_data):
        return student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data['name']
        instance.roll = validated_data['roll']
        instance.city = validated_data['city']
        instance.save()
        return instance