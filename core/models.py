from django.db import models
from users.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    rating = models.FloatField(editable=False,null=True,blank=True,default=0)
    rate_counter = models.IntegerField(default=0,editable=False)


    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField()
    rate = models.PositiveIntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)])

@receiver(post_save,sender=Comment)
def add_book_rate(sender, instance, created, **kwargs):
    if created:
        #Book rating
        rating      = float(instance.book.rating)
        counter     = int(instance.book.rate_counter)+1
        new_rate    = instance.rate + rating
        new_rating  = new_rate/counter
        instance.book.rating = new_rating
        instance.book.rate_counter = counter
        instance.book.save()