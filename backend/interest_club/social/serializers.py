from rest_framework import serializers
from django.shortcuts import get_object_or_404

from social.models import SocialGroup, GroupRecord, Comment
from users.serializers import UserSummarySerializer


class SocialGroupSerializer(serializers.ModelSerializer):
    owner = UserSummarySerializer(read_only=True)
    users = UserSummarySerializer(many=True, read_only=True)
    class Meta:
        model = SocialGroup
        fields = ['id', 'owner', 'users', 'name', 'summary', 'description', 'logo']
        read_only_fields = ['id', 'owner', 'users']
        

class SocialGroupIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialGroup
        fields = ['id',]


class GroupRecordSerializer(serializers.ModelSerializer):
    owner = UserSummarySerializer(read_only=True)
    group = SocialGroupIdSerializer()
    class Meta:
        model = GroupRecord
        fields = ['id', 'owner', 'group', 'name', 'description', 'created_date', 'event_date']
        read_only_fields = ['id', 'owner', 'created_date']

    def create(self, validated_data):
        print(validated_data)
        return GroupRecord.objects.create(
            owner=validated_data.get('owner'),
            group=get_object_or_404(SocialGroup, pk=validated_data.get('group')['id']),
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            created_date=validated_data.get('created_date'),
            event_date=validated_data.get('event_date'),
        )


class GroupRecordNoGroupSerializer(serializers.ModelSerializer):
    owner = UserSummarySerializer(read_only=True)
    group = SocialGroupIdSerializer(read_only=True)
    class Meta:
        model = GroupRecord
        fields = ['id', 'owner', 'group', 'name', 'description', 'created_date', 'event_date']
        read_only_fields = ['id', 'owner', 'created_date', 'group']


class GroupRecordIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRecord
        fields = ['id',]


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSummarySerializer(read_only=True)
    parent = GroupRecordSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'parent', 'text', 'created_date']
        read_only_fields = ['id', 'owner', 'created_date']


class CommentNoParentSerializer(serializers.ModelSerializer):
    owner = UserSummarySerializer(read_only=True)
    parent = GroupRecordSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'parent', 'text', 'created_date']
        read_only_fields = ['id', 'owner', 'created_date', 'parent']


class CommentIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id',]