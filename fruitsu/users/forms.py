from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="ваш адрес", required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user