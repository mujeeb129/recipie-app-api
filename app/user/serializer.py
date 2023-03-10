"""
Serializer module for serializing data
"""
from rest_framework import serializers

from django.contrib.auth import get_user_model

def error_response(error):
    return {'Error': error}


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
