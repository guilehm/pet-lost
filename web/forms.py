from django import forms

from users.models import User


class AuthenticationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('password',)
