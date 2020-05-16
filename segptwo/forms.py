from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('usernmae')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password=password)
            if not user:
                raise forms.ValidationError('this user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError("This user is not active")


        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    
    email = forms.EmailField(label='Email Address')
    # email2 = forms.EmailField(label='Confirm Address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = (
            'username',
            'email',
            # 'email2',
            'password',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # email2 = self.cleaned_data.get('email2') #self.cleaned_data.get('email1')


        if email!= email:
            raise forms.ValidationError(
            'emails must match'
        )

        email_qs = User.objects.filter(email=email)
        if email_qs:
            raise forms.ValidationError(
            'This email has already been used'
        )

        return email