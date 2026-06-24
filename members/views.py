from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# 1. 補上缺少的 members 函數
def members(request):
    mymembers = Member.objects.all() # 這裡不需要 .values()，直接拿物件比較好處理
    return render(request, 'all_members.html', {'mymembers': mymembers})

def details(request, id):
    mymember = get_object_or_404(Member, id=id)
    return render(request, 'details.html', {'mymember': mymember})

def main(request):
    return render(request, 'library.html')

# 2. 確保 new_member 只有一個，且使用 form.save()
def new_member(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() # 這裡會自動建立 User 並存入 Member
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "new_member.html", {"form": form})

def new_member_result(request):
    return HttpResponse('This is the result page for adding a new member')

def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == "POST":
        member.delete()
        return redirect("members")
    return render(request, 'delete_member.html', {'member': member})

def library(request):
    return render(request, 'library.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "帳號或密碼錯誤"})
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("/login")
