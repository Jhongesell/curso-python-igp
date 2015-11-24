from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()

html = """
<div class="alert alert-%s alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>Alerta!</strong> %s
</div>
"""

@register.filter
@stringfilter
def alerta(value, severity='warning'):
    return mark_safe(html % (severity, value))
#alerta.is_safe = True


#register.filter('alerta', alerta)