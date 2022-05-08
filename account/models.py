from django.contrib.auth.models import User
from django.db import models

USER_TYPE = [
    ("STUDENT", "Student"),
    ("MENTOR_OR_STUDENT", 'Mentor')
]


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, null=False)
    profile_image = models.ImageField(upload_to='profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default="STUDENT")

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name='No Name')
        return obj.pk

    def __str__(self):
        return self.user.id

    class Meta:
        db_table = 'auth_employee'
