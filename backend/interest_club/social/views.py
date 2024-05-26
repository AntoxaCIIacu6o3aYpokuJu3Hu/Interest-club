import datetime

from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from drf_spectacular.utils import extend_schema, extend_schema_view

from social.models import SocialGroup, GroupRecord, Comment
from social.serializers import SocialGroupSerializer, SocialGroupIdSerializer
from social.serializers import GroupRecordSerializer, GroupRecordNoGroupSerializer
from social.serializers import CommentSerializer, CommentNoParentSerializer
from social.permissions import IsOwnerOrReadOnly


@extend_schema_view(
    get=extend_schema(
        summary="Get a list of social groups",
    ),
    post=extend_schema(
        summary="Create a new social group",
    ),
)
class SocialGroupList(generics.ListCreateAPIView):
    queryset = SocialGroup.objects.all()
    serializer_class = SocialGroupSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user, users=[user])
    

@extend_schema_view(
    get=extend_schema(
        summary="Get social group by id",
    ),
    put=extend_schema(
        summary="Update social group by id",
    ),
    patch=extend_schema(
        summary="Partialy update social group by id",
    ),
    delete=extend_schema(
        summary="Delete social group by id",
    ),
)
class SocialGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialGroup.objects.all()
    serializer_class = SocialGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


class SocialGroupMembership(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SocialGroupIdSerializer

    @extend_schema(summary="Join social group by id")
    def post(self, request, format=None):
        user = request.user
        group_id = request.data['id']
        group = get_object_or_404(SocialGroup, pk=group_id)
        group.users.add(user)
        group.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    
    @extend_schema(summary="Leave social group by id")
    def put(self, request, format=None):
        user = request.user
        group_id = request.data['id']
        group = None
        try:
            group = SocialGroup.objects.get(pk=group_id)
        except:
            return Response(request.data, status=status.HTTP_204_NO_CONTENT)
        group.users.remove(user)
        group.save()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)
    

@extend_schema_view(
    get=extend_schema(
        summary="Get a list of all group records",
    ),
    post=extend_schema(
        summary="Create a new group record",
    ),
)
class GroupRecordList(generics.ListCreateAPIView):
    queryset = GroupRecord.objects.all()
    serializer_class = GroupRecordSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user, created_date=datetime.datetime.now().isoformat())
    

@extend_schema_view(
    get=extend_schema(
        summary="Get group record by id",
    ),
    put=extend_schema(
        summary="Update group record by id",
    ),
    patch=extend_schema(
        summary="Partialy update group record by id",
    ),
    delete=extend_schema(
        summary="Delete group record by id",
    ),
)
class GroupRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupRecord.objects.all()
    serializer_class = GroupRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    

@extend_schema_view(
    get=extend_schema(
        summary="Get a list of all coments",
    ),
    post=extend_schema(
        summary="Create a new comment",
    ),
)
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user, created_date=datetime.datetime.now().isoformat())
    

@extend_schema_view(
    get=extend_schema(
        summary="Get comment by id",
    ),
    put=extend_schema(
        summary="Update comment by id",
    ),
    patch=extend_schema(
        summary="Partialy update comment by id",
    ),
    delete=extend_schema(
        summary="Delete comment by id",
    ),
)
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentNoParentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
