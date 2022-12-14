from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Poll, Choice, Vote
from rest_framework.authtoken.models import Token

class VoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vote
        fields = '__all__'
        
class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required= False)
    
    class Meta:
        model = Choice
        fields = '__all__'
        
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = Poll
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validate_data):
        user = User(
            email = validate_data['email'],
            username = validate_data['username']
        )
        user.set_password(validate_data['password'])
        user.save()
        Token.objects.create(user = user)
        
        return user
    