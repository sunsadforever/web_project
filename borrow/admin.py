from django.contrib import admin
from .models import BorrowRecord

# 客製化後台顯示畫面
class BorrowRecordAdmin(admin.ModelAdmin):
    # 在後台列表清單中要顯示哪些欄位
    list_display = ('id', 'get_username', 'book_id', 'borrow_date')
    
    # 支援透過書本 ID 搜尋
    search_fields = ('book_id', 'user__username')

    # 因為 user 是外鍵，定義一個方法來顯示 username
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = '會員帳號'

# 註冊模型與客製化後台設定
admin.site.register(BorrowRecord, BorrowRecordAdmin)