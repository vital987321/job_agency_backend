from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_authenticated:
            if view.action == 'list':
                return False
            if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
                return True
        return False
        
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_authenticated:
            return obj == request.user
        return False



class ApplicationPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        # the rest is for authorized not_staff users
        if view.action == 'list':
            return True
        elif view.action in ['create', 'retrieve', 'destroy']:  
            return True
        elif view.action in ['update', 'partial_update']:
            return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        if view.action in ['create', 'retrieve', 'destroy']:
            return obj.user==request.user
            # return True
        return False


class VacancyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        # Uuthorized or Anonimous user
        if view.action == 'list':
            return True
        if view.action == 'retrieve':
            return True
        return False
    def has_boject_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        # Uuthorized or Anonimous user
        if view.action == 'retrieve':
            return True
        return False
    
class PartnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return False

class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.user.is_authenticated:
            return True
        # Anonimous User
        if view.action in ['list', 'retrieve']:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.user.is_authenticated:
            if view.action in ['retrieve','create']:
                return True
            if view.action in ['update', 'partial_update', 'destroy']:
                return obj.user==request.user
        # Anonimous User
        if view.action =='retrieve':
            return True
        return False
    
class SectorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if view.action in ['list', 'retreive']:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if view.action =='retreive':
            return True
        return False