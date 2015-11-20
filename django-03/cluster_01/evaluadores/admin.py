from django.contrib import admin
from cluster_01.admin import admin_site

# Register your models here.

from evaluadores.models import Evaluador

class EvaluadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'created')

admin_site.register(Evaluador, EvaluadorAdmin)
