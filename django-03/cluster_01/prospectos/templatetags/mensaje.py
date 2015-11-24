from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


html = '<div class="alert alert-%s" role="alert">%s</div>'
register = template.Library()

@register.filter
def mensaje(texto, severidad='success'):
    return mark_safe(html % (severidad, texto))


#register.filter('mensaje', mensaje)
