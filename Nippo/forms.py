from django import forms
from .models import DailyReportModel
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Firstname',min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message='Only letters is allowed !')],
        widget=forms.TextInput(attrs={'placeholder':'Enter FirstName...'})
    )

    last_name = forms.CharField(
        label='Lastname',min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message='Only letters is allowed !')],
        widget=forms.TextInput(attrs={'placeholder':'Enter LastName...'})
    )

    username = forms.CharField(
        label='Username',min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s0-9]*$',message='Only letters is allowed !')],
        widget=forms.TextInput(attrs={'placeholder':'Enter UserName ...'})
    )

    email =forms.CharField(
        label='Email Address',min_length=8,max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message='Put a valid Email Address !')],
        widget=forms.TextInput(attrs={'placeholder':'Enter vaild Email Address...'})

    )
    password1 = forms.CharField(
        label='Password',min_length=8, max_length=16,
        widget=forms.PasswordInput(attrs={'placeholder':'Enter Password...'}) 
    )
    password2 = forms.CharField(
        label='Confirm Password',min_length=8, max_length=16,
        widget=forms.PasswordInput(attrs={'placeholder':'Enter Password...'}) 
    )
    group_choices =(
        ('M','Manager'),
        ('U','User'),
        ('E','Employee'),
    )
    groups = forms.ChoiceField(choices=group_choices)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password1','password2']

class DailyReportForm(forms.ModelForm):
    
    topic = forms.CharField(
        label='Topic',min_length=5,max_length=200,
        # validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message='Only letters is allowed !')],
        # required=False,
        widget=forms.TextInput(attrs={'placeholder':'Enter Topic.....'})
    )
    content = forms.CharField(
        label='Content',min_length=10,max_length=200,
        # validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message='Only letters is allowed !')],
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Enter Content.....'})
    )

    report = forms.CharField(
        label='Report',min_length=10,max_length=200,
        # validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message='Only letters is allowed !')],
        # required=False,
        widget=forms.Textarea(attrs={'placeholder':'Enter What you did Today.....','rows':4})
    )

    comment = forms.CharField(
        label='Comment',min_length=10,max_length=200,
        # validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message='Only letters is allowed !')],
        # required=False,
        widget=forms.Textarea(attrs={'placeholder':'Enter Your opinion.....','rows':4})
    )

    class Meta:
        model = DailyReportModel
        fields = ['topic','content','report','comment']

    # def __init__(self, *args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         UneditableField('text_input', css_class='form-control-lg')
    #     )
    # Validation on form
# Name: ^[a-zA-ZÀ-ÿ\s]*$
# Email: ^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$
# Age: ^[0-9]*$