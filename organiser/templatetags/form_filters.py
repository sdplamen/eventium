from django import template

register = template.Library()

@register.filter
def readonly(field):
    return field.as_widget(attrs={'readonly': 'readonly'})
