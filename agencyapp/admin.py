from django.contrib import admin
from agencyapp.models import User, Field, Vacancy, Application

admin.site.register(User)
admin.site.register(Field)
admin.site.register(Vacancy)
admin.site.register(Application)