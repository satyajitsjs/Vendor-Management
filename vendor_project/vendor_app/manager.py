from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, name, password=None):
        if not email and not phone:
            raise ValueError('Users must have an email address or phone number')
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, name, password=None):
        user = self.create_user(
            email,
            phone,
            name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
