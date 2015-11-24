from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

html = """
<div class="progress">
  <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="%s" aria-valuemin="0" aria-valuemax="100" style="width: %s%% ">
     <span class="sr-only">%s%% Complete</span>
  </div>
</div>
"""



@register.simple_tag
@stringfilter
def progbar(p=50):
    return html % (p, p, p)



