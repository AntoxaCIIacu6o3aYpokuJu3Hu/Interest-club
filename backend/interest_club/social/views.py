from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from drf_spectacular.utils import extend_schema, extend_schema_view

from social.models import SocialGroup, GroupRecord, Comment
from social.serializers import SocialGroupSerializer, SocialGroupMembershipSerializer
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
    serializer_class = SocialGroupMembershipSerializer

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
    