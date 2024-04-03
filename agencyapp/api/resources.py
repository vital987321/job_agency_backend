from rest_framework import viewsets
from agencyapp.api.serializers import UserSerializer, VacancySerializer, SectorSerializer, ApplicationSerializer
from agencyapp.models import Vacancy, Application, User
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class VacancyViewSet(viewsets.ModelViewSet):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer
    filter_backends=[DjangoFilterBackend]
    filter_fields=('name')
    


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer