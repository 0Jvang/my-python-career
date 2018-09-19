from django import forms
from app1.models import User

# class LoginForm(forms.Form):
#     name = forms.CharField(max_length=20)
#     password = forms.CharField(max_length=1, widget=forms.PasswordInput(attrs={'class':'passwd'}))


class LoginForm(forms.ModelForm):
    # 元信息
    class Meta:
        model = User
        fields = '__all__'
