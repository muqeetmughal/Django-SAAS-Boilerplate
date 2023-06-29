from django.db.models.signals import post_save
from django.dispatch import receiver
from tenants import models as tenant_models

from django_tenants.signals import schema_migrated
from django_tenants.utils import schema_context
from django.db import transaction
from authentication.models import UserAccount


@receiver(schema_migrated)
def create_tenant_credentials(sender, **kwargs):
    print("Signal after Migrations completed called to create super user")

    schema_name = kwargs["schema_name"]
    
    if schema_name != 'public':

        tenant: tenant_models.Tenant = tenant_models.Tenant.objects.filter(
            schema_name=schema_name
        ).first()

        with schema_context(schema_name):
            user = UserAccount.objects.filter(email=tenant.email).first()
            if user:
                print(f"Tenant Superuser {tenant.name} already exists")
                return
            else:
                with schema_context(schema_name):
                    with transaction.atomic():
                        try:
                            user = UserAccount(
                                email=tenant.email,
                                phone_number=tenant.phone_number,
                                name=tenant.name,
                            )
                            user.set_password("12345678")

                            user.is_superuser = True
                            user.is_staff = True

                            user.save()

                            # warehouse = tenant_models.Warehouse(name="Default Location")
                            # warehouse.is_current = True
                            # warehouse.save()
                        except Exception as e:
                            print("Exception",e)
                            # tenant.delete()
