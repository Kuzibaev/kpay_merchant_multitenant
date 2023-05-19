from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.choices import UserType


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.type == UserType.USER)


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.type == UserType.SUPER_USER)


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.type == UserType.SUPER_USER
        )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
