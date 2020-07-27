from django.forms import ModelForm

from apps.authapp.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.cleaned_data['password']
