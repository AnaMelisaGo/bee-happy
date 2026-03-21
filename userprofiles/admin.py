from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Add Profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display username and email
    fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)
