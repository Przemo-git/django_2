from django import template

from apartments.models import Apartment

register = template.Library()

from django.utils.safestring import mark_safe




@register.filter
def colorize(val):
    if Apartment.objects.filter(activated=True):
        mark = str(val)[2]
        if mark < str(val)[2:]:
            html_string = f"<span style='color:black'>{val} zł</span"
        else:
            html_string = f"<span style='color:green'>{val} zł</span"
        return mark_safe(html_string)
