from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class SignupForm(UserCreationForm):
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자, 공백 입력 불가',
    }))
    user_name = forms.CharField(label='이름')
    phone_number = forms.CharField(label='핸드폰 번호')
    Gender = (
        ('성별', '성별'),
        ('남성', '남성'),
        ('여성', '여성'),
    )
    gender = forms.ChoiceField(label='성별', choices=Gender)
    birth_date = forms.DateField(label='생년월일')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('동일한 번호가 이미 존재합니다.')
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('사용중인 이메일입니다.')
        return email

    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            user_name=self.cleaned_data['user_name'],
            birth_date=self.cleaned_data['birth_date'],
            gender=self.cleaned_data['gender'],
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
        )
        return user
