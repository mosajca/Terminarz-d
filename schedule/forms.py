from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
            send_mail('Aktywuj konto',
                      'http://127.0.0.1:8000/activate/{}/{}'.format(user.pk, default_token_generator.make_token(user)),
                      'admin', [user.email])
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Ten email został już użyty.')
        return self.cleaned_data['email']
