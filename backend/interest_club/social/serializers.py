from rest_framework import serializers

from social.models import SocialGroup, GroupRecord, Comment


class SocialGroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SocialGroup
        fields = ['id', 'owner', 'users', 'name', 'summary', 'description', 'logo']