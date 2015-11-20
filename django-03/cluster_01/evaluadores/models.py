from django.db import models
from base.models import UserModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Evaluador(UserModel):

    class Meta:
        verbose_name = _(u'Evaluador')
        verbose_name_plural = _(u'Evaluadores')
