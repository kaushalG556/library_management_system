from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    book_upload = models.FileField(upload_to="pdf/")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self) -> str:
        return self.title
    
class Borrower(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    borrow_date = models.DateField()
    fine = models.IntegerField()
    returned = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='No')

    def __str__(self):
        return self.name