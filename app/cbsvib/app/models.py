from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    avatar = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(blank=True, max_length=8, unique=True)
    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


class Organization(models.Model):
    title = models.CharField(max_length=12, unique=True)
    description = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, unique=True)
    postcode = models.IntegerField(unique=True)
    users = models.ForeignKey(UserProfile, blank=True, null=True, related_name='organization',
                              on_delete=models.CASCADE)

    def __str__(self):
        return "Organization " + str(self.title)


class Event(models.Model):
    title = models.CharField(max_length=12, unique=True)
    description = models.CharField(max_length=255, unique=True, blank=True)
    organizations = models.ManyToManyField(Organization, blank=True)
    image = models.ImageField(blank=True)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return "Event " + str(self.title)
