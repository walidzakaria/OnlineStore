from django.forms import ModelForm

from .models import Purchase, Order
from apps.authapp.models import User


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

    def clean_created_by(self):
        if not self.cleaned_data['created_by']:
            return User()
        return self.cleaned_data['created_by']

    def clean_updated_by(self):
        if not self.cleaned_data['updated_by']:
            return User()
        return self.cleaned_data['updated_by']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_created_by(self):
        if not self.cleaned_data['created_by']:
            return User()
        return self.cleaned_data['created_by']

    def clean_updated_by(self):
        if not self.cleaned_data['updated_by']:
            return User()
        return self.cleaned_data['updated_by']


