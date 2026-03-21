from django.contrib import admin
from django.contrib.auth.models import Group

# Unregister group --- codemy.com
admin.site.unregister(Group)