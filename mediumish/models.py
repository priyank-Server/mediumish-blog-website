# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(email=self.normalize_email(email), date_of_birth=date_of_birth, )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, date_of_birth, password=None):
#         user = self.create_user(email, password=password, date_of_birth=date_of_birth, )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True, )
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin
#
#     @property
#     def is_superuser(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Blog', default=True)
    image = models.ImageField()
    slug = AutoSlugField(populate_from=['title'], null=True, blank=True)

    def __str__(self):
        return self.title
