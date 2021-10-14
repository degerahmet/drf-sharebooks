from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from core.models import Writer,Publisher
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','username')
        extra_kwargs = {'email': {'read_only': True}}



class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=150, required=True)
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self,email):
        user = User.objects.filter(email=email)
        if user:
            raise serializers.ValidationError(
                'Email address is already registered.'
            )
        
        return email
    
    def validate_username(self,username):
        user = User.objects.filter(username=username)
        if user:
            raise serializers.ValidationError(
                'Username address is already registered.'
            )
        
        return username


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=500, required=True)

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = [
            'id',
            'name',
            'description'
        ]

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            'id',
            'title',
        ]