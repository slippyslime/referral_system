from rest_framework import serializers
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'invite_code', 'referred_by']
        read_only_fields = ['id', 'phone_number', 'invite_code']
