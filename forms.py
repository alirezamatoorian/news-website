from django import forms
from .models import *


class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش'),
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11, required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError("شماره تلفن عددی نیست!")
            else:
                return phone


class CommentForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            if len(name) < 3:
                raise forms.ValidationError("نام کوتاه است")
            else:
                return name

    class Meta:
        model = Comment
        fields = ['name', 'body']


class SearchForm(forms.Form):
    query = forms.CharField()


class CreatePostForm(forms.ModelForm):
    image1 = forms.ImageField(label="تصویر اول")
    image2 = forms.ImageField(label="تصویر دوم")

    class Meta:
        model = Post
        fields = ['title', 'description', 'reading_time', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "con-name",

            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '5',
            }),
            'reading_time': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),

        }


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=250, required=True)
#     password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)

class Register_form(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd['password2']:
            raise forms.ValidationError('پسورد ها یکی نیست')
        return cd["password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", 'email']


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bio', "jop",'photo','date_of_birth']
