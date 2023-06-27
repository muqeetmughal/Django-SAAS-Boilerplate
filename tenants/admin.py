from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from tenants.models import Tenant, Domain


class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1


@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("email", "paid_until", "on_trial", "is_active", "is_verified")
    inlines = [DomainInline]


admin.site.register(Domain)