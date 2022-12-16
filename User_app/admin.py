from django.contrib import admin
from .import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserCreationForm,UserChangeForm
# User = get_user_model()
#
# class UserAdmin(BaseUserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     list_display = ('first_name', 'last_name', 'email','password', 'mobile', 'user_name', 'image', 'gender'
#                   ,'is_active', 'is_staff', 'is_admin')
#     list_filter =('is_admin',)
#     fieldsets = (
#         (
#             None,{
#                 'fields':('first_name', 'last_name', 'email','password', 'mobile', 'user_name', 'image', 'gender')
#             }
#         ),
#         (
#             'permission',{
#                 'fields':('is_staff', 'is_admin')
#             }
#         )
#     )
#     add_fieldsets =(
#         (
#             None, {
#                 'fields': ( 'first_name', 'last_name', 'email', 'password1','password2','mobile', 'user_name', 'image', 'gender')
#             }
#         ),
#         (
#             'permission', {
#                 'fields': ('is_staff', 'is_admin')
#             }
#         )
#     )
#     search_fields = ('first_name', 'last_name', 'email',)
#     ordering = ('mobile',)
#
# admin.site.register(User,UserAdmin)

# @admin.register(CustomUser,UserAdmin)
# # class UserAdmin(admin.ModelAdmin):
# #     list_display = ('email','mobile','password','image')
admin.site.register(models.UserProfile)