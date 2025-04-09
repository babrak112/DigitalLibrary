from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, PasswordInput, Textarea, DateField, NumberInput


from accounts.models import Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ("username","first_name","last_name","email","password1","password2")

    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Confirm Password', widget=PasswordInput)
    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Date of birth", required=False)
    biography = CharField(widget=Textarea,label="Bio",required=False)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        date_of_birth = self.cleaned_data.get('date_of_birth')
        biography = self.cleaned_data.get('biography')
        profile = Profile(
            user=user,
            date_of_birth=date_of_birth,
            first_name=user.first_name,
            last_name=user.last_name,
            bio=biography
        )
        if commit:
            profile.save()
        return user







