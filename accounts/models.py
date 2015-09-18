from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from authwrap.mixins import UserMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=email)
        user.assign_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, UserMixin):

    USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin
