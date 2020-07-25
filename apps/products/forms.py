from django.forms import ModelForm

from .models import Product
from apps.authapp.models import User


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_created_by(self):
        if not self.cleaned_data['created_by']:
            return User()
        return self.cleaned_data['created_by']

    def clean_updated_by(self):
        if not self.cleaned_data['updated_by']:
            return User()
        return self.cleaned_data['updated_by']