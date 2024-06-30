from django_filters import rest_framework as filters
from agencyapp.models import Vacancy, Application
from django.db.models import Q
from rest_framework import filters as rf_filters
from django_filters.rest_framework import DjangoFilterBackend

class VacancyFilterSet(filters.FilterSet):
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
        
class VacancyListDjangoFilterBackend(DjangoFilterBackend):
    """
    For uses filters active vacancies
    For staff filters active vacancies (default)
        or returns all vacancies (active and not)
    """
    def filter_queryset(self, request, queryset, view):
        if request.user.is_staff:
            if 'active' in request.query_params.keys():
                if request.query_params['active']=='false':
                    return super().filter_queryset(request, queryset, view)
        query_set=super().filter_queryset(request, queryset, view)
        return query_set.filter(active=True)


class IsOwnerFilterBackend(rf_filters.BaseFilterBackend):
    """
    Allows users to see only their own objects
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)


class AdminOrIsOwnerDjangoFilterBackend(DjangoFilterBackend):
    """
    DjangoFilterBackend
    Admin (staff) has access to all objects.
    user has access only to his own objects.
    """

    def filter_queryset(self, request, queryset, view):
        if request.user.is_staff:
            return super().filter_queryset(request, queryset, view)
        qery_set=super().filter_queryset(request, queryset, view)
        return qery_set.filter(user=request.user)

    
class ApplicationFilterSet(filters.FilterSet):
    id=filters.NumberFilter(field_name='id', lookup_expr='exact')
    vacancy_id=filters.NumberFilter(field_name="vacancy", lookup_expr='exact')
    email=filters.CharFilter(field_name="email", lookup_expr='icontains')
    status=filters.CharFilter(field_name='status', lookup_expr='icontains')
    vacancy_name=filters.CharFilter(method='vacancy_name_filter')
    company=filters.CharFilter(method='company_filter')
    user_id=filters.NumberFilter(field_name='user', lookup_expr='exact')
    first_name=filters.CharFilter(method='user_first_name_filter')
    last_name=filters.CharFilter(method='user_last_name_filter')
    phone=filters.CharFilter(method='phone_filter')

    class Meta:
        model=Application
        fields=[]

    def vacancy_name_filter(self, queryset, query_name, value):
        return queryset.filter(vacancy__name__icontains=value)
    
    def company_filter(self, queryset, query_name, value):
        return queryset.filter(vacancy__company__icontains=value)
    
    def user_first_name_filter (self, queryset, query_name, value):
        return queryset.filter(first_name__icontains=value)
    
    def user_last_name_filter (self, queryset, query_name, value):
        return queryset.filter(last_name__icontains=value)
    
    def phone_filter(self, queryset, query_name, value):
        if not value:
            return queryset
        number=''.join([symbol for symbol in value if symbol.isnumeric()])
        return queryset.filter(phone__icontains=number)