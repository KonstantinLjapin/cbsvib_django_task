from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
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
    title = serializers.CharField(max_length=12, default='friendly')
    description = serializers.CharField(max_length=255, default='circle')
    address = serializers.CharField(max_length=255, default='Saint-Petersburg')
    postcode = serializers.IntegerField(max_value=999999, default=125480)

    class Meta:
        model = Organization
        permission_classes = [IsAuthenticated]
        fields = '__all__'

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.email)
        instance.description = validated_data.get('description', instance.email)
        instance.address = validated_data.get('address', instance.content)
        instance.postcode = validated_data.get('postcode', instance.created)
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    pass

