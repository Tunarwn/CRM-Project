from django.contrib import admin
from .models import Record, Profile
# Register your models here.

admin.site.register(Record)
admin.site.register(Profile)

# superuser account
# Username : admin
# pass : admin1234