from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            # return request.user.is_authenticated and request.user.is_admin
            return True
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False
                                                                                                
    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_admin
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_admin
        elif view.action == 'destroy':
            return obj == request.user or request.user.is_admin
        else:
            return False


class ApplicationPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        print('__________________')
        print('has_permission')
        print(view.action)
        print(request.user.is_authenticated)
        print(f'check Create: {view.action == "create"}')
        print('__________________')
        if not request.user.is_authenticated:
            print('inside request.user.is_authenticated')
            return False
        print('pass request.user.is_authenticated')
        if request.user.is_staff:
            return True
        print('pass user.is_staff')
        if view.action=='list':
            print('inside view.action==list')
            return True
        
        
        elif view.action == 'create':
            print('inside view.action==create')
            return True
        elif view.action in ['retrieve', 'destroy']:
            print('inside view.action in retrieve, destroy')
            return True
        elif view.action in ['update', 'partial_update']:
            print('inside view.action in update, partial_update')
            return False
        else:
            print('inside else')
            return False
    
    def has_object_permission(self, request, view, obj):
        print()
        print('__________________')
        print('has_object_permission')
        print(view.action)
        print(request.user.is_authenticated)
        print(request.user.is_staff)
        print('__________________')
        print()
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        if view.action in ['create','retrieve','destroy']:
            return True
        return False
        