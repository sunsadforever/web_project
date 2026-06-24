from django.db import models
from django.contrib.auth.models import User

class BookManager(models.Manager):
    def get_available_books(self):
        return self.filter(is_borrowed=False)

class Book(models.Model):
    name = models.CharField(max_length=100)
    book_code = models.CharField(max_length=50)
    is_borrowed = models.BooleanField(default=False)
    
    # 預設管理器，確保所有查詢都正常
    objects = models.Manager()
    # 自訂管理器，專門用於篩選架上書籍
    available_objects = BookManager()

    def __str__(self):
        return self.name

class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)