from rest_framework import viewsets
from agencyapp.api.serializers import UserSerializer, VacancySerializer, SectorSerializer, ApplicationSerializer
from agencyapp.models import Vacancy, Application, User
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from agencyapp.api.filters import VacancyFilter

class VacancyViewSet(viewsets.ModelViewSet):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=VacancyFilter

# class VacancyViewSet(viewsets.ModelViewSet):
#     queryset=Vacancy.objects.all()
#     serializer_class=VacancySerializer
#     filter_backends=[DjangoFilterBackend]
#     # filterset_fields=['name', 'location']
#     filterset_fields={'name':["icontains","exact"], "location":["exact"]}
    


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     print()
    #     print('Request:')
    #     user=request.user
    #     print(user.id)
    #     print()
    #     return super().list(self, request, *args, **kwargs)