from django.db import models
from django.contrib.auth import models as auth_model


class CustomUserManager(auth_model.BaseUserManager):

    def create_user(self, email: str, username: str, password: str = None, is_staff = False, is_superuser = False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")

    
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self, email: str, username: str, password: str = None):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(auth_model.AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True, blank=False)
    username = models.CharField(verbose_name="username", max_length=255, blank=False)
    password = models.CharField(verbose_name="password", max_length=255, blank=False)
    image = models.ImageField(verbose_name="image", upload_to='users/%Y/%m/%\d/', blank=True)
    bio = models.TextField(
        verbose_name="bio", 
        blank=True, null=True, 
        editable=True, 
        help_text="Let your followers know more about you"
        )
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    
    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm: str, obj: None) -> bool:
        return True

    def has_module_perms(self, app_label: str) -> bool:
        return True
    
    @property
    def is_staff(self):
        return self.is_admin