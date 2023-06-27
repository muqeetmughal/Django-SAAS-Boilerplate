from django.db import models
from django_tenants.models import DomainMixin, TenantMixin

class Tenant(TenantMixin):
    company_name = models.CharField(max_length=50, blank=True, null=True)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField()
    is_verified = models.BooleanField(default=False)
    company_info = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=13, null=True)
    auto_create_schema = True
    auto_drop_schema = True

    class Meta:
        ordering = ('-featured', '-updated_at')
        db_table = 'tenants'

    def __str__(self):
        return f"{self.email}"


class Domain(DomainMixin):
    pass

