from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from social.models import SocialGroup, GroupRecord, Comment
from social.serializers import SocialGroupSerializer #, GroupRecordSerializer, CommentSerializer


class SocialGroupList(APIView):
    def get(self, request, format=None):
        social_groups = SocialGroup.objects.all()
        serializer = SocialGroupSerializer(social_groups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SocialGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SocialGroupDetail(APIView):
    def get_object(self, pk):
        try:
            return SocialGroup.objects.get(pk=pk)
        except SocialGroup.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        social_group = self.get_object(pk)
        serializer = SocialGroupSerializer(social_group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        social_group = self.get_object(pk)
        serializer = SocialGroupSerializer(social_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        social_group = self.get_object(pk)
        social_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)