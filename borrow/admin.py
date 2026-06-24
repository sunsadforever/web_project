from django.contrib import admin
from .models import Book, BorrowRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 在後台列表頁面顯示的欄位
    list_display = ('name', 'is_borrowed')
    # 允許在列表頁面直接編輯這些欄位
    list_editable = ('is_borrowed',)
    # 搜尋功能
    search_fields = ('name',)

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    # 顯示借閱紀錄的詳細資訊
    list_display = ('user', 'book', 'borrow_date', 'returned')
    list_filter = ('returned', 'borrow_date')