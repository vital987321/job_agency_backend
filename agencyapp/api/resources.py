from rest_framework import viewsets
from agencyapp.api.serializers import UserSerializer, VacancySerializer, SectorSerializer, ApplicationSerializer
from agencyapp.models import Vacancy, Application, User, Sector
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from agencyapp.api.filters import VacancyFilter, IsOwnerFilterBackend
from rest_framework import permissions
from agencyapp.api.permissions import UserPermission
from agencyapp.api.pagination import LargeResultsSetPagination

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class VacancyViewSet(viewsets.ModelViewSet):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=VacancyFilter


class SectorViewSet(viewsets.ModelViewSet):
    serializer_class=SectorSerializer
    queryset=Sector.objects.all()
    pagination_class=LargeResultsSetPagination



class ApplicationViewSet(viewsets.ModelViewSet):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer
    filter_backends=[IsOwnerFilterBackend]

    def perform_create(self, serializer):
        if 'use_profile_cv' in self.request.data.keys():
            if self.request.data['use_profile_cv']:
                user_cv=serializer.validated_data['user'].cv 
                serializer.save(cv=user_cv)
            else:
                serializer.save()
        else:
            serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [UserPermission]


    
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })