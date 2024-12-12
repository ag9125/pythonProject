from django import forms
from Olxapp.models import Olx,Image
from multiupload.fields import MultiFileField
class SellForm(forms.ModelForm):
    more_images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
    class Meta:
        model = Olx
        fields = ['title', 'category', 'SET_A_PRICE', 'Description', 'Upload_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'SET_A_PRICE': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Upload_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class UpdateForm(forms.ModelForm):
    more_images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
    class Meta:
        model = Olx
        fields = ['title', 'category', 'SET_A_PRICE', 'Description', 'Upload_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'SET_A_PRICE': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Upload_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
