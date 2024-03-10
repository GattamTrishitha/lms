from django.db import models

# Create your models here.
class BooksDetails(models.Model):
    Book_title =models.CharField(max_length=255)
    Book_price=models.CharField(max_length=255)
    Book_type=[
        ('Thirller','Thirller'),
        ('Rom-Com','Rom-Com'),
        ('Mystery','Mystery'),
        ('Motivational','Motivational'),
    ]
    Book_type=models.CharField(max_length=20, choices=Book_type)
    Book_Author=models.CharField(max_length=255)
    About=models.TextField()
    def __str__(self):
        return self.Book_title