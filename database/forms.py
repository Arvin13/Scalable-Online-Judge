from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

class NewUserForm(forms.ModelForm):

    username = forms.CharField(label='Username',required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder' : 'Username'}))
    first_name = forms.CharField(label="First Name",required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'First Name'}))
    last_name = forms.CharField(label="Last Name",required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Last Name'}))
    email = forms.CharField(label="email",required=True,max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Email'}))
    password = forms.CharField(label="Password",required=True,max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Password'}))
    re_password = forms.CharField(label="Re-Password",required=True,max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Reenter Password'}))
    

    class Meta:
        model = User
        fields = (
            "username",
            "email", 
            "password", 
            "first_name", 
            "last_name",)
    
    def check_name(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            return False
        return True
    
    def check_mail(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email = email).exists():
            return False
        return True
    
    def create_new_user(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        new_user = User.objects.create_user(username,email,password)

        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.date_joined = timezone.now()
        new_user.is_active = False
        new_user.save()

        return 'new user created'