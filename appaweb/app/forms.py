from django.forms import ModelForm
from django import forms
from .models import Order,Comment
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class orderForm(ModelForm):
 name = forms.CharField(label='نام\n', label_suffix="",widget=forms.TextInput(attrs={'size':5}))
 email = forms.EmailField(label='ایمیل\n', label_suffix="",widget=forms.TextInput(attrs={'size':5}))
 phone = forms.IntegerField(label=' تلفن\n', label_suffix="",widget=forms.TextInput(attrs={'size':5}))


 class Meta:

     model = Order
     fields = ('name','email','phone')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',label='نام ')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',label='ایمیل')
    phone = forms.IntegerField(help_text='Required',label='شماره تلفن')
    username=forms.CharField(label='نام کاربری')
    class Meta:
        model = User
        fields = ('username','first_name', 'phone','email', 'password1', 'password2', )

class LoginForm(AuthenticationForm):

     class Meta:
        model = User
        fields = ('username', 'password' )


class commentForm(ModelForm):
    comment=forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":26}),label='' , label_suffix="")
    class Meta:
        model=Comment
        fields=('comment',)