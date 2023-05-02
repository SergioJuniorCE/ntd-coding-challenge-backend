from django.db import models

from users.models import User
from operations.models import Operation


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    operation = models.OneToOneField(Operation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_balance = models.DecimalField(max_digits=10, decimal_places=2)
    operation_response = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
