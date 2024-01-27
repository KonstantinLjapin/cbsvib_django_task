from rest_framework import serializers
from .models import UserProfile, Organization, Event


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password', 'avatar')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class OrganizationSerializer(serializers.ModelSerializer):
    pass


class EventSerializer(serializers.ModelSerializer):
    pass

