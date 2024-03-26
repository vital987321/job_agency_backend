from rest_framework import viewsets
from agencyapp.api.serializers import UserSerializer, VacancySerializer, SectorSerializer, ApplicationSerializer
from agencyapp.models import Vacancy, Application, User

class VacancyViewSet(viewsets.ModelViewSet):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer