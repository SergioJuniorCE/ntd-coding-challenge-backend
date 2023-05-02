from django.db import models

# Create your models here.
class Operation(models.Model):
    # addition, subtraction, multiplication, division, square_root, random_string
    OPERATION_TYPES = [
        ('addition', 'addition'),
        ('subtraction', 'subtraction'),
        ('multiplication', 'multiplication'),
        ('division', 'division'),
        ('square_root', 'square_root'),
        ('random_string', 'random_string')
    ]
    
    id = models.AutoField(primary_key=True)
    op_type = models.CharField(choices=OPERATION_TYPES, max_length=30)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.id}, {self.op_type}, {self.cost}"