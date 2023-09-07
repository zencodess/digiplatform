from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import AccountManager, ServiceProvider, Service, Customer, Ordering


class UserAdmin(BaseUserAdmin):
    # The forms to add and change account manager instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the account manager model
    list_display = ('email', 'name', 'date_joined', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password')}
        ),
    )
    # add_fieldsets get_fieldsets to use this attribute when creating a account manager.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(AccountManager, UserAdmin)
admin.site.unregister(Group)
admin.site.register([ServiceProvider, Service, Customer, Ordering])