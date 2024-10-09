from django import forms 
from home.models import Product,Category,User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Product Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Product Name'

    }))
    description= forms.CharField(label='Product Description',widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Enter Product Description'

    }))
    image = forms.ImageField(label='Product Image',widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',

    }))
    category = forms.ModelChoiceField(label='Category Name',queryset=Category.objects.all(),
                                      empty_label = "Select Category", 
                                      widget=forms.Select(attrs={
                                      'class': 'form-control'
    }))
    price =  forms.IntegerField(label='Rate',widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder':'Enter Rate of Product '


    }))
    stock = forms.IntegerField(label='Qty Available',widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Enter the Qty'
        
    }))


    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name','description']
        # exclude = ['stock']

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter the Category Name'
    }))
    class Meta:
        model = Category
        fields = '__all__' 

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter First Name'

    }))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Last Name'

    }))
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Username'

    }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Email Address'

    }))
    password1 = forms.CharField(label='Paswword',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Password'

    }))
    password2 = forms.CharField(label='Paswword',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm Your Password'

    }))
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100,required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Username'

    }))
    password = forms.CharField(label='Password',max_length=100,required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Password'

    }))

