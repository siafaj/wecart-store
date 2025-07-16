from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Your Password',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
                'placeholder': 'Enter Your First Name',
            })
        self.fields['last_name'].widget.attrs.update({
                'placeholder': 'Enter Your Last Name',
            })
        self.fields['email'].widget.attrs.update({
                'placeholder': 'Enter A Valid Email',
            })
        self.fields['phone_number'].widget.attrs.update({
                'placeholder': 'Enter Your Phone Number',
            })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

