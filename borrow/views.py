from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Book, BorrowRecord
from .forms import BookForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

@login_required
def borrow_book(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "只接受 POST"}, status=405)

    book_id = request.POST.get("book_id")
    
    try:
        with transaction.atomic():
            # 鎖定該書，避免同時被借出
            book = Book.objects.select_for_update().get(id=book_id)
            
            if book.is_borrowed:
                return JsonResponse({"success": False, "message": "這本書已經被別人借走了"})

            book.is_borrowed = True
            book.save()

            BorrowRecord.objects.create(user=request.user, book=book)
            
        return JsonResponse({"success": True, "message": "借閱成功！"})

    except Book.DoesNotExist:
        return JsonResponse({"success": False, "message": "找不到這本書"})

@login_required
def return_book(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "只接受 POST"}, status=405)

    book_id = request.POST.get("book_id")
    
    with transaction.atomic():
        # 找到該使用者借閱中且未歸還的紀錄
        record = BorrowRecord.objects.select_for_update().filter(
            book_id=book_id,
            user=request.user,
            returned=False
        ).first()

        if not record:
            return JsonResponse({"success": False, "message": "您沒有借閱這本書，或已經歸還過了"})

        record.returned = True
        record.save()

        # 更新書籍狀態
        book = record.book
        book.is_borrowed = False
        book.save()

    return JsonResponse({"success": True, "message": "歸還成功！"})
def is_admin(user):
    return user.is_authenticated and user.is_staff # 通常用 is_staff 判斷管理員權限
def library_view(request):
    # 【測試模式】不分權限，強制抓取資料庫所有書籍
    all_books = Book.objects.all()
    print(f"DEBUG: 資料庫總共有 {all_books.count()} 本書")
    
    # 判斷邏輯暫時先註解掉，強制只傳 books 進去
    books = all_books
    
    return render(request, 'library.html', {'books': books})
@user_passes_test(is_admin, login_url='/login/')
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library') # 存完跳回圖書館頁面
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
# borrow/views.py
from django.conf import settings
