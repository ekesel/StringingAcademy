from django import template

register = template.Library()

@register.simple_tag
def my_set_tag(value):
    return set(value)
