from django.forms import ValidationError
from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    def create(self, clean_data):
        user = UserModel.objects.create_user(
            username=clean_data['username'],
            password=clean_data['password']
        )
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()
    def check_user(self, clean_data):
        user = authenticate(
            username=clean_data['username'],
            password=clean_data['password']
        )
        if not user:
            raise ValidationError('User not found')
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'balance']