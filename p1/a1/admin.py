from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from a1.models import contact, UserCreationForm
# Register your models here.

admin.site.register(contact)
class CustomUserAdmin(UserAdmin):
    # Customize the appearance and behavior of the User model in the admin interface
    # For example, you can specify which fields are displayed, readonly fields, fieldsets, etc.

# Register the custom admin class for the User model
    admin.site.unregister(User)  # Unregister the default UserAdmin
admin.site.register(User, CustomUserAdmin)  # Register the CustomUserAdmin instead