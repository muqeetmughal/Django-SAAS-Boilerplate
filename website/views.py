from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .forms import *
from tenants.models import Tenant
from django_tenants.utils import schema_context
from django.db import transaction
from authentication.models import UserAccount
from django.utils import timezone
from tenants.models import Tenant, Domain


def home(request):
    context = {}

    form = StartTrialForm()

    context["form"] = form

    return render(request, "index.html", context)


def start_trial(request):
    if request.method == "POST":
        form = StartTrialForm(request.POST)

        if form.is_valid():
            validated_data = form.cleaned_data
            email = validated_data["email"]

            tenant = Tenant.objects.filter(email=email).first()

            if tenant:
                return JsonResponse(
                    {"msg": f"Client Already Exist", "success": False},
                )

            schema_name = str(validated_data["company_name"]).lower().replace(" ", "")
            # generated_password = f"12345678"

            with schema_context(schema_name):
                user = UserAccount.objects.filter(email=email).first()
                if user:
                    return JsonResponse({"msg": f"Email Already Exist", "success": False})

            with transaction.atomic():
                tenant = Tenant(
                    name=validated_data["name"],
                    schema_name=schema_name,
                    paid_until=timezone.now() + timezone.timedelta(days=14),
                    company_name=validated_data["company_name"],
                    # company_info=validated_data["company_info"],
                    on_trial=True,
                    is_active=True,
                    email=email,
                )
                tenant.save()
                domain = Domain()
                domain.domain = str(schema_name)
                domain.tenant = tenant
                domain.is_primary = True
                domain.save()

            return JsonResponse({"msg": "Successfully Registered", "success": True})
        else:
            return JsonResponse(form.errors)
