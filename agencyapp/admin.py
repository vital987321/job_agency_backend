from django.contrib import admin
from agencyapp.models import User, Sector, Vacancy, Application

admin.site.register(User)
admin.site.register(Sector)
admin.site.register(Vacancy)
admin.site.register(Application)