from django import forms
from django.contrib.auth.models import User
from .models import Member
from datetime import date

class RegisterForm(forms.ModelForm):
    # 1. 明確定義密碼欄位，並加上 label 增加易讀性
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="密碼"
    )

    class Meta:
        model = Member
        fields = ["username", "password", "phone", "joined_date"]
        widgets = {
            # 2. 如果你想限制年份範圍，可以在這裡加 years 參數，預設會是今年前後幾年
            "joined_date": forms.SelectDateWidget()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 3. 正確動態帶入今天的日期作為初始值
        self.fields["joined_date"].initial = date.today()

    # 4. 【關鍵修正】覆寫 save 方法，確保密碼被加密（雜湊化）
    def save(self, commit=True):
        member = super().save(commit=False)
        # 假設你的 Member 模型有繼承 User，或者有 set_password 方法
        if hasattr(member, 'set_password'):
            member.set_password(self.cleaned_data["password"])
        else:
            # 如果是完全自訂的模型且沒繼承 User，請確保你的密碼有加密邏輯
            pass
            
        if commit:
            member.save()
        return member