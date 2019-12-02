from django import forms
from first_app.models import WebPage
from django.contrib.auth.models import User
from first_app.models import UserProfileInfos


# Email Form for register
class EmailForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    vmail = forms.EmailField(max_length=100, label='Confirm Email ')
    text = forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['vmail']

        if email != vmail:
            raise forms.ValidationError("Email not Conformed")


# for post user
class PostForm(forms.ModelForm):

    class Meta:
        model = WebPage
        fields = ('top', 'url', 'name')

    def clean(self):
        all_clean = super().clean()
        return all_clean


# for profile user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfos
        fields = ('potfolio_site','profile_pic')
