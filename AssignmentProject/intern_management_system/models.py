from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INTERN = "INTERN", "Intern"
        EMPLOYEE = "EMPLOYEE", "Employee"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class InternManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INTERN)


class Intern(User):

    base_role = User.Role.INTERN

    intern = InternManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Interns"


@receiver(post_save, sender=Intern)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "INTERN":
        InternProfile.objects.create(user=instance)


class InternProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intern_id = models.IntegerField(null=True, blank=True)


class EmployeeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.EMPLOYEE)


class Employee(User):

    base_role = User.Role.EMPLOYEE

    employee = EmployeeManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Employees"


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Employee)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "EMPLOYEE":
        EmployeeProfile.objects.create(user=instance)