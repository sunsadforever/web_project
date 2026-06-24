from django.urls import path
from . import views

# borrow/urls.py (或是你定義路徑的地方)
urlpatterns = [
    # 加上 name='borrow_book' 這一點非常重要！
    path("borrow/", views.borrow_book, name='borrow_book'), 
    path('add_book/', views.add_book_view, name='add_book'),
    path('', views.library_view, name='library'),
]