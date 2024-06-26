from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','id', 'profile_pic', 'phone_number','is_verified']



