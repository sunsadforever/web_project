from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="借閱會員")
    book_id = models.IntegerField(verbose_name="書本 ID")
    borrow_date = models.DateTimeField(auto_now_add=True, verbose_name="借閱時間")

    def __str__(self):
        return f"{self.user.username} 借閱了書本 ID: {self.book_id}"
    # 其他欄位...
# Create your models here.
