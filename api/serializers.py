from rest_framework import serializers
import datetime
from api.models import Todo


class TodoSerializer(serializers.Serializer):
    task = serializers.CharField(required=True)
    is_completed = serializers.BooleanField(default=False)
    time = serializers.DateTimeField(default=datetime.datetime.now())

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance
    

