from rest_framework import serializers
from .models import User

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'image', 'bio')