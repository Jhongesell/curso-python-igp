# -*- coding: utf8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User, Group

ADMIN_SITE_TITLE = _(u'Sistema de Gestión del Cluster')

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ADMIN_SITE_TITLE

    # Text to put in each page's <h1>.
    site_header = ADMIN_SITE_TITLE

    # Text to put at the top of the admin index page.
    index_title = ADMIN_SITE_TITLE

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin_site = MyAdminSite()
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
