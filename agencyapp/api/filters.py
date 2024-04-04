from django_filters import rest_framework as filters
from agencyapp.models import Vacancy
from django.db.models import Q

class VacancyFilter(filters.FilterSet):
    key_search=filters.CharFilter(method='name_or_description')
    location=filters.CharFilter(field_name='location', lookup_expr='icontains')
    salary_gte=filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_lte=filters.NumberFilter(field_name='salary', lookup_expr='lte')
    residence_type=filters.NumberFilter(field_name='residence_type', lookup_expr='gte')
    
    class Meta:
        model=Vacancy
        fields=[]
 
    def name_or_description(self, queryset, query_name, value):
        return queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))
        


