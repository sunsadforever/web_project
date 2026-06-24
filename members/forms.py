from django import forms
from django.contrib.auth.models import User
from .models import Member

class RegisterForm(forms.ModelForm):
    # 新增這兩個欄位給 User 用
    username = forms.CharField(label="帳號")
    password = forms.CharField(widget=forms.PasswordInput(), label="密碼")

    class Meta:
        model = Member
        fields = ["username", "password", "phone"]

    def save(self, commit=True):
        # 1. 先建立 User (Django 會自動處理密碼加密)
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"]
        )
        
        # 2. 建立 Member 並關聯剛剛建立的 user
        member = Member(
            user=user, 
            phone=self.cleaned_data["phone"]
        )
        if commit:
            member.save()
        return member