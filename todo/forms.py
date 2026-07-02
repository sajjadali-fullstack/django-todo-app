from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            }
        ))

    conform_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        }
    ))


    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username/Name', 'class': 'form-control'}),
        }

        def clean(self, *args, **kwargs):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            conform_password = cleaned_data.get('conform_password')

            if password != conform_password:
                raise forms.ValidationError('Passwords do not match')
            return cleaned_data