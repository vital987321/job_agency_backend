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
    application_id=filters.NumberFilter(field_name='id', lookup_expr='exact')

    class Meta:
        model=Application
        fields=[]