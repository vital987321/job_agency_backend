from django.db import models
from job_agency_backend.settings import CONTRACT_TYPE, RESIDENCE_TYPES, APPLICATION_STATUS
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    cv = models.FileField(upload_to='media\cv', blank=True, null=True)
    def __str__(self) -> str:
        return 'id:'+str(self.id)  + ' | ' + (self.username)

class Sector(models.Model):
    name=models.CharField(max_length=100, unique=True)
    def __str__(self) -> str:
        return 'id:'+str(self.id)  + ' | ' +   'Sector: '+str(self.name)
    

class Vacancy(models.Model):
    name=models.CharField(max_length=200)
    sector=models.ManyToManyField(Sector, blank=True, related_name='vacancies')
    location = models.CharField(max_length=300, blank=True, null=True)
    salary=models.PositiveIntegerField(blank=True, null=True)
    company=models.CharField(max_length=100, blank=True, null=True)
    contract_type = models.CharField(
        max_length=100, choices=CONTRACT_TYPE, default=CONTRACT_TYPE[0][0])
    hours_from = models.TimeField(blank=True, null=True)
    hours_to = models.TimeField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=[
                            ('Male/Female', 'Male/Female'),
                              ('Male', 'Male'),
                              ('Female', 'Female')], 
                              default='Male/Female')
    description=models.TextField(max_length=1000, blank=True, null=True)
    requirements = models.TextField(max_length=1000, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    residence_type = models.IntegerField(choices=RESIDENCE_TYPES, blank=True, null=True)
    # residence_type = models.CharField(max_length=100, choices=RESIDENCE_TYPES, blank=True, null=True)
    visa_assistance=models.BooleanField(null=True, blank=True)
    active=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural='vacancies'
        ordering=['-created_at']

    def __str__(self):
        if len(self.name)<30:
            name=str(self.name)
        else:
            name=self.name[:28]+'...'
        if self.location:
            location = self.location
        else:
            location='-'
        return 'id:'+str(self.id)  + ' | ' +  name + ' | ' + location + ' | ' + str(self.salary) + ' | ' + str(self.created_at)
       
    

class Application(models.Model):
    vacancy=models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', blank=True, null=True)
    first_name=models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone=models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(max_length=1000, blank=True, null=True)
    cv = models.FileField(upload_to='media\cv', blank=True, null=True)
    status=models.CharField(max_length=50, choices=APPLICATION_STATUS, default=APPLICATION_STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']

    def __str__(self):
        vacancy=self.vacancy.name
        if len(self.vacancy.name)<30:
            vacancy=str(self.vacancy.name)
        else:
            vacancy=self.vacancy.name[:28]+'...'

        if self.user:
            user=self.user.username
        else:
            user=self.email

        return 'id:'+str(self.id)  + ' | ' +   vacancy + ' | ' + user + ' | ' + str(self.created_at)
