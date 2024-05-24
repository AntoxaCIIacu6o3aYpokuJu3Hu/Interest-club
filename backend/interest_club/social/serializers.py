from rest_framework import serializers

from social.models import SocialGroup, GroupRecord, Comment
from users.serializers import UserSummarySerializer


class SocialGroupSerializer(serializers.ModelSerializer):
    owner = UserSummarySerializer(read_only=True)
    users = UserSummarySerializer(many=True, read_only=True)
    class Meta:
        model = SocialGroup
        fields = ['id', 'owner', 'users', 'name', 'summary', 'description', 'logo']
        read_only_fields = ['id', 'owner', 'users']
        
class SocialGroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialGroup
        fields = ['id',]