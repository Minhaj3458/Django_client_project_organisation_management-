from django.contrib import admin
from .import models
from .import forms
# Register your models here.


class List_personal(admin.ModelAdmin):
    add_form = forms.Personal_InfoForm
    # list_display = ('email', 'phone1', 'phone2', 'address',)
    # list_filter = ('address',)
    # search_fields = ('email', 'phone1', 'phone2', 'address',)
    fieldsets = (
        (
            None, {
                'fields': ('email', 'phone1',)
            }
        ),

    )


admin.site.register(models.Personal_Info)
