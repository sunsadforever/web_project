from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='library'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/new_member', views.new_member, name='new_member'),
    path('members/new_member_result', views.new_member_result, name='new_member'),
    path("members/delete/<int:id>", views.delete_member, name="delete_member"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),

    #path("members/library", views.library, name="library"),

]