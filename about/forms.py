from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from about.models import Profile


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     address=forms.CharField(max_length=50)
#     Phone=forms.CharField(max_length=50)
#     class Meta:
#         model = User
#         fields = ['username', 'email','address']


# class ProfileUpdateForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['image']


# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm




# from django import forms
# from .models import ShippingAddress

# class ShippingForm(forms.ModelForm):
# 	shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}), required=True)
# 	shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=True)
# 	shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=True)
# 	shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address2'}), required=False)
# 	shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True)
# 	shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
# 	shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=False)
# 	shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True)

# 	class Meta:
# 		model = ShippingAddress
# 		fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']

# 		exclude = ['user',]


# class UserInfoForm(forms.ModelForm):
# 	phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False)
# 	address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=False)
# 	address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
# 	city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
# 	state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
# 	zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=False)
# 	country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)

# 	class Meta:
# 		model = Profile
# 		fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', )



# class ChangePasswordForm(SetPasswordForm):
# 	class Meta:
# 		model = User
# 		fields = ['new_password1', 'new_password2']

# 	def _init_(self, *args, **kwargs):
# 		super(ChangePasswordForm, self)._init_(*args, **kwargs)

# 		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
# 		self.fields['new_password1'].label = ''
# 		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

# 		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
# 		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
# 		self.fields['new_password2'].label = ''
# 		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# class UpdateUserForm(UserChangeForm):
# 	# Hide Password stuff
# 	password = None
# 	# Get other fields
# 	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=False)
# 	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), required=False)
# 	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), required=False)

# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email')

# 	def _init_(self, *args, **kwargs):
# 		super(UpdateUserForm, self)._init_(*args, **kwargs)

# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
# 		self.fields['username'].label = ''
# 		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image',
        ]