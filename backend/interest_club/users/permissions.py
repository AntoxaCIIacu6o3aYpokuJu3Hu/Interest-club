from rest_framework import permissions

class IsThatUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == 'POST' or obj == request.user or request.user.is_staff
    