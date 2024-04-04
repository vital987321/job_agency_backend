from django_filters import rest_framework as filters
from agencyapp.models import Vacancy

class VacancyFilter(filters.FilterSet):
    name=filters.CharFilter(field_name='name', lookup_expr='icontains')
    location=filters.CharFilter(field_name='location', lookup_expr='icontains')
    salary_gte=filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_lte=filters.NumberFilter(field_name='salary', lookup_expr='lte')
    residence_type=filters.NumberFilter(field_name='residence_type', lookup_expr='gte')
    class Meta:
        model=Vacancy
        fields=['name', 'location', 'salary_gte', 'salary_lte','residence_type']



