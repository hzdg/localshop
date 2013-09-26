from django.contrib import admin

from localshop.apps.permissions import models


class CidrAdmin(admin.ModelAdmin):
    list_display = ['cidr', 'label']


class CredentialAdmin(admin.ModelAdmin):
    list_display = ['creator', 'access_key', 'created', 'comment']


class HostnameAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Hostname, HostnameAdmin)
admin.site.register(models.CIDR, CidrAdmin)
admin.site.register(models.Credential, CredentialAdmin)
