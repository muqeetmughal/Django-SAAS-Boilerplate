from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password, name=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            name=name,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=150)
    phone_number = models.CharField(max_length=13, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # boss = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="staff")

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email
