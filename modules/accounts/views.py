from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserAccountForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "users_list.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    form_class = UserAccountForm
    template_name = "user_form.html"
    success_url = reverse_lazy("users-list")


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAccountForm
    template_name = "user_form.html"
    success_url = reverse_lazy("users-list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "user_confirm_delete.html"
    success_url = reverse_lazy("users-list")
