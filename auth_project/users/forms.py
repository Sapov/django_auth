from django import forms
from .models import *


class Profiles(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')

# class UploadFiles(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['material', "quantity", 'width', 'length', 'path_file']


# class OrdersAdd(forms.ModelForm):
#     class Meta:
#         model = Orders
#         fields = ('__all__')


# class UploadArhive(forms.ModelForm):
#     class Meta:
#         model = UploadArhive
#         fields = ('__all__')
