from django import template

register = template.Library()

from django.utils.safestring import mark_safe




@register.filter
def colorize(val):
    mark = str(val)[2]
    if mark < str(val)[2:]:
        html_string = f"<span style='color:black'>{val} zł</span"
    else:
        html_string = f"<span style='color:green'>{val} zł</span"
    return mark_safe(html_string)