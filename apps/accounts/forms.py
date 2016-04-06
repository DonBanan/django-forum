from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext as _

from .models import User


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=_('Login or E-Mail'))


class SingUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'required'}, render_value=False),
                                label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'required'}, render_value=False),
                                label=_('Password (again)'))

    def clean_username(self):
        if User.objects.filter(username__iexact=self.cleaned_data['username']):
            raise forms.ValidationError(_("This username is already in use. Please supply a different username."))
        return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(
                _("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_('Passwords do not match!'))
        return self.cleaned_data

    def save(self, commit=True):
        user = super(SingUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        exclude = ['last_login', 'is_staff', 'is_active', 'date_joined', 'password',
                   'user_permissions', 'is_superuser', 'groups', 'raw_password', 'vote', 'is_moderator', 'rank']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['last_login', 'username', 'is_staff', 'is_active', 'date_joined', 'password',
                   'user_permissions', 'is_superuser', 'groups', 'raw_password', 'vote', 'is_moderator', 'rank', 'password1', 'password1']