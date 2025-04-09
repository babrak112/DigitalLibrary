from django.contrib.auth.models import User
from django.db.models import Model, CASCADE, OneToOneField, DateField, TextField, CharField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    date_of_birth = DateField(null=True, blank=True)
    first_name = CharField(max_length=50, null=True, blank=True)
    last_name = CharField(max_length=50, null=True, blank=True)
    bio = TextField(null=True, blank=True)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"Profile {self.user.username}"


    def __str__(self):
        return self.user.username
