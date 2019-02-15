from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def cleaned_user_email(self):
        username = self.cleaned_data('username')
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Email address already registered")
        return email

        if password1 != password2:
            raise ValidationError("Passwords don't match")

        if not password1 or not password2:
            raise ValidationError("Please enter your password again")

        return password1
