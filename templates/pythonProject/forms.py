from django import forms
class usersForm(forms.Form):
    num1=forms.CharField(label="Value1",widget=forms.Textarea(attrs={'class':"form-control"}))
    num2=forms.CharField(label="Value2",widget=forms.TextInput(attrs={'class':"form-control"}))
    Email=forms.EmailField()
    