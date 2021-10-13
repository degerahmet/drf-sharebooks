from django.db import models
from users.models import User
# Create your models here.


class Writer(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return f"{self.name}"


class Publisher(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.title}"


class Book(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="books")
    name = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE,related_name="books")
    place_of_publication = models.CharField(max_length=200,null=True,blank=True)
    date_of_publication = models.DateField()
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name="books")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="books")
    summary = models.TextField()

    def __str__(self):
        return f"{self.name}"


    