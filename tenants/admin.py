from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from tenants.models import Tenant, Domain
from django_tenants.utils import get_public_schema_name
from django.apps import apps
# from django.contrib.sites.models import Site
class PublicTenantOnlyMixin:
        """Allow Access to Public Tenant Only."""
        def _only_public_tenant_access(self, request):
                return True if request.tenant.schema_name == get_public_schema_name() else False
        
        def has_view_permission(self,request, view=None):
                return self._only_public_tenant_access( request)
        
        def has_add_permission(self,request, view=None):
                return self._only_public_tenant_access(request)
        
        def has_change_permission(self,request, view=None):
                return self._only_public_tenant_access( request)
        
        def has_delete_permission(self,request, view=None):
                return self._only_public_tenant_access( request)
        
        def has_view_or_change_permission(self,request, view=None):
                return self._only_public_tenant_access( request)
        

class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1


@admin.register(Tenant)
class TenantAdmin(PublicTenantOnlyMixin,TenantAdminMixin, admin.ModelAdmin):
    list_display = ("email", "paid_until", "on_trial", "is_active", "is_verified")
    inlines = [DomainInline]


@admin.register(Domain)
class DomainAdmin(PublicTenantOnlyMixin, TenantAdminMixin, admin.ModelAdmin):
    pass



# admin.site.unregister(Site)
# admin.autodiscover()
