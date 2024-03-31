from rest_framework import serializers
from agencyapp.models import User, Vacancy, Sector, Application

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(read_only=True)
    
    class Meta:
        model=User
        fields=['username','first_name', 'last_name', 'email', 'phone', 'cv', ]
    
    def validate_email(self, value):
        if len(User.objects.filter(email=value))>=1:
            raise serializers.ValidationError('User with such email already exists.')
        return value

    def save(self):
        super().save(username=self.validated_data['email'])


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sector
        fields=['name',]   


class VacancySerializer(serializers.ModelSerializer):
    created_at=serializers.DateTimeField(read_only=True)
    sector_name = SectorSerializer(many=True, read_only=True, source='sector')

    class Meta:
        model=Vacancy
        fields=['id',
                'name',
                'sector',
                'location', 
                'salary', 
                'company',
                'contract_type',
                'hours_from',
                'hours_to',
                'gender',
                'description', 
                'requirements', 
                'created_at', 
                'residence_type', 
                'visa_assistance',
                'sector_name']



class ApplicationSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model=Application
        fields=['vacancy',
                'user',
                'phone', 
                'email', 
                'message',
                'cv', 
                'status',
                'created_at',
                'first_name',
                'last_name'
                 ]

