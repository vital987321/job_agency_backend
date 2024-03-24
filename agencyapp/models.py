from django.db import models
from job_agency_backend.settings import CONTRACT_TYPE, RESIDENCE_TYPES, APPLICATION_STATUS
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15)
    cv = models.FileField(upload_to='media\cv', blank=True, null=True)


class Field(models.Model):
    name=models.CharField(max_length=100)
    

class Vacancy(models.Model):
    name=models.CharField(max_length=200)
    field=models.ForeignKey(Field, on_delete=models.CASCADE, related_name='vacancies')
    location = models.CharField(max_length=300, blank=True, null=True)
    salary=models.PositiveIntegerField(blank=True, null=True)
    company=models.CharField(max_length=100, blank=True, null=True)
    contract_type = models.CharField(
        max_length=100, choices=CONTRACT_TYPE, default=CONTRACT_TYPE[0][0])
    description=models.TextField(max_length=1000, blank=True, null=True)
    created_at=models.DateField(auto_now_add=True)
    residence_type = models.CharField(max_length=100, choices=RESIDENCE_TYPES, blank=True, null=True)
    visa_assistance=models.BooleanField(null=True, blank=True)

class Application(models.Model):
    vacancy=models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', blank=True, null=True)
    phone=models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(max_length=1000, blank=True, null=True)
    cv = models.FileField(upload_to='media\cv', blank=True, null=True)
    status=models.CharField(max_length=50, choices=APPLICATION_STATUS, default=APPLICATION_STATUS[0][0])


