from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User


# Create your forms here.


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control',}))
    
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control',}))
    
    username = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    email = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'form-control',}))
    
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control','data-toggle': 'password','id': 'password',}))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control','data-toggle': 'password','id': 'password',}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']








class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))

    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control','data-toggle': 'password','id': 'password','name': 'password',}))

    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']



def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError ("A user with that username already exists.")


# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user