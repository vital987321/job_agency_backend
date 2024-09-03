from django_filters import rest_framework as filters
from agencyapp.models import Vacancy, Application
from django.db.models import Q
from rest_framework import filters as rf_filters
from django_filters.rest_framework import DjangoFilterBackend

class PartnerFilterSet(filters.FilterSet):
    company=filters.CharFilter(field_name='company', lookup_expr='icontains')
    hr_name=filters.CharFilter(field_name='hr_name', lookup_expr='icontains')
    phone=filters.CharFilter(method='phone_filter')

    def phone_filter(self, queryset, query_name, value):
        if not value:
            return queryset
        number=''.join([symbol for symbol in value if symbol.isnumeric()])
        return queryset.filter(phone__icontains=number)


class ReviewFilterSet(filters.FilterSet):
    user=filters.NumberFilter(field_name='user', lookup_expr='exact')
    rating=filters.NumberFilter(field_name='rating', lookup_expr='exact')
    comment=filters.CharFilter(field_name='comment', lookup_expr='icontains')
    first_name=filters.CharFilter(method='get_name')
    last_name=filters.CharFilter(method='get_last_name')
    email=filters.CharFilter(method='get_email')

    def get_name(self, queryset, query_name, value):
        return queryset.filter(user__first_name__icontains=value)
    
    def get_last_name(self, queryset, query_name, value):
        return queryset.filter(user__last_name__icontains=value)
    
    def get_email(self, queryset, query_name, value):
        return queryset.filter(user__email__icontains=value)



class VacancyFilterSet(filters.FilterSet):
    key_search=filters.CharFilter(method='name_or_description')
    location=filters.CharFilter(field_name='location', lookup_expr='icontains')
    salary_gte=filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_lte=filters.NumberFilter(field_name='salary', lookup_expr='lte')
    residence_type=filters.NumberFilter(field_name='residence_type', lookup_expr='gte')
    name=filters.CharFilter(field_name='name', lookup_expr='icontains')
    company=filters.CharFilter(method='company_admin')
    id=filters.NumberFilter(field_name='id', lookup_expr='exact')
    sector=filters.CharFilter(method='vacancy_sector_name')
    favourite=filters.BooleanFilter(method='get_favourites')
    
    class Meta:
        model=Vacancy
        fields=[]
 
    def name_or_description(self, queryset, query_name, value):
        return queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))
    
    def company_admin(self, queryset, query_name, value):
        if self.request.user.is_staff:
            return queryset.filter(partner__company__icontains=value)
        return queryset
    
    def vacancy_sector_name(self, queryset, query_name, value):
        return queryset.filter(sector__name__icontains=value)
    
    def get_favourites(self, queryset, query_name, value):
        if value:
            return queryset.filter(users=self.request.user)
        return queryset
    


class VacancyListDjangoFilterBackend(DjangoFilterBackend):
    """
    For users: filters active vacancies
    For staff: filters active vacancies (default)
                or returns all vacancies (active and not)
    """

    def filter_queryset(self, request, queryset, view):
        query_set=super().filter_queryset(request, queryset, view)
        if request.user.is_staff:
            if 'active' in request.query_params.keys():
                if request.query_params['active']=='all':
                    return query_set
                if request.query_params['active']=='deactivated':
                    return query_set.filter(active=False)
                if request.query_params['active']=='active':
                    return query_set.filter(active=True)
            return query_set
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
        if request.user.is_anonymous:
            return qery_set.none()
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
        return queryset.filter(vacancy__partner__company__icontains=value)
    
    def user_first_name_filter (self, queryset, query_name, value):
        return queryset.filter(first_name__icontains=value)
    
    def user_last_name_filter (self, queryset, query_name, value):
        return queryset.filter(last_name__icontains=value)
    
    def phone_filter(self, queryset, query_name, value):
        if not value:
            return queryset
        number=''.join([symbol for symbol in value if symbol.isnumeric()])
        return queryset.filter(phone__icontains=number)