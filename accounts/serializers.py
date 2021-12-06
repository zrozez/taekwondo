from rest_framework import serializers

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
