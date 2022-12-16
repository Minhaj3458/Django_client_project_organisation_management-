from django import template
from Admin_app.models import Personal_Info,Social_Media

register = template.Library()


@register.simple_tag
def personal_info():
    return Personal_Info.objects.all().order_by('-id')[:1]

@register.simple_tag
def social_media():
    return Social_Media.objects.all().order_by('-id')[:1]

# @register.simple_tag
# def ecom_set():
#     return Setting.objects.get(id=1)