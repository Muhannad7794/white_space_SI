from rest_framework import serializers


# A general serializer for parsing data
class ServerASerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    hobbies = serializers.ListField(child=serializers.CharField(max_length=100))
