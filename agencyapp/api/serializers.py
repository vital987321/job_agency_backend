from rest_framework import serializers
from agencyapp.models import User, Vacancy, Sector, Application

class UserSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=150, required=True)
    # last_name = serializers.CharField(max_length=150, required=True)
    id=serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True, required=True, max_length=100)
    
    class Meta:
        model=User
        fields=['id','username','first_name', 'last_name', 'email', 'phone', 'cv', 'password', 'favourites' ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user

    def validate_email(self, value):
        if self.context['request'].method=="POST" and len(User.objects.filter(email=value))>=1:
            raise serializers.ValidationError('User with such email already exists.')
        return value
    
    def validate_phone(self, value):
        if not value:
            return ''
        allowed_phone_symbols='+0123456789'
        for symbol in str(value):
            if not symbol in allowed_phone_symbols:
                 raise serializers.ValidationError(f"Incorrect phone format. Allowed symbols: '{allowed_phone_symbols}'. Symbol '{symbol}' is not allowed.")
        return value

    def save(self):
        if self.context['request'].method=="POST":
            super().save(username=self.validated_data['email'])
        else:
            super().save()


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sector
        fields=['id', 'name',]   


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
                'sector_name',
                'active',
                ]




class ApplicationSerializer(serializers.ModelSerializer):
    vacancy_details=VacancySerializer(read_only=True, source='vacancy')
    user_details=UserSerializer(read_only=True, source='user')
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model=Application
        fields=['id',
                'vacancy',
                'vacancy_details',
                'user',
                'user_details',
                'phone', 
                'email', 
                'message',
                'cv', 
                'status',
                'created_at',
                'first_name',
                'last_name'
                 ]
        
    def validate_phone(self, value):
        if not value:
            return ''
        allowed_phone_symbols='+0123456789'
        for symbol in str(value):
            if not symbol in allowed_phone_symbols:
                 raise serializers.ValidationError(f"Incorrect phone format. Allowed symbols: '{allowed_phone_symbols}'. Symbol '{symbol}' is not allowed.")
        return value

        