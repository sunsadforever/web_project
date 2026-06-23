from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import RegisterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
    # 使用 render 函式，並務必把第一個參數 request 傳進去！
    return render(request, 'library.html')
def new_member(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # 或你想去的頁面
    else:
        form = RegisterForm()

    return render(request, "new_member.html", {
        "form": form
    })
def new_member_result(request):
  return HttpResponse('This is the result page for adding a new member')
def delete_member(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == "POST":
        member.delete()
        return redirect("members")
def library(request):
    return render(request, 'library.html')
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                "login.html",
                {"error": "帳號或密碼錯誤"}
            )

    return render(request, "login.html")
