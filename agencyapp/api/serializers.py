from rest_framework import serializers
from agencyapp.models import User, Vacancy, Sector, Application

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['phone', 'cv', ]

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model=Vacancy
        fields=['name',
                'sector',
                'location', 
                'salary', 
                'company',
                'contract_type', 
                'description', 
                'requirements', 
                'created_at', 
                'residence_type', 
                'visa_assistance']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sector
        fields=['name',]

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields=['vacancy',
                'user',
                'phone', 
                'email', 
                'message',
                'cv', 
                'status', 
                 ]