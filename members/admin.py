from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # fields 定義了在編輯頁面中要出現哪些欄位
    fields = ('user', 'phone', 'role', 'joined_date')
    
    # 唯讀欄位：建議將 joined_date 設為唯讀，因為它是 auto_now_add
    readonly_fields = ('joined_date',)
    
    # list_display 定義了在清單頁面要顯示的欄位
    list_display = ('user', 'phone', 'role', 'joined_date')

# 如果你沒有用 @admin.register，可以用這種寫法：
# admin.site.register(Member, MemberAdmin)
