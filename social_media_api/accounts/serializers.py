from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']   
      

    def create(self, validated_data):
        user = get_user_model().objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        token, created = Token.objects.create(user=user)
        return user     
    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['id', 'username', 'email', 'followers']    