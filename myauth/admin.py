from django.contrib import admin
from myauth.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
# now you must add """ AUTH_PROFILE_MODULE = 'myauth.UserProfile' """ in you settings.py file.
