from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length = 200,help_text = "Enter book genre")
    def __str__(self):
        return self.genre

class Author(models.Model):
    name = models.CharField(max_length = 50,help_text = "Enter author name")
    country = models.CharField(max_length=50,help_text = "Enter author's country")
    image = models.CharField(max_length = 200,help_text= "Enter the image url",null=True)
    description = models.CharField(max_length=500,help_text="Enter the description",null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100,help_text = "Enter book title")
    author = models.ForeignKey(Author,on_delete = models.SET_NULL,null = True)
    isbn = models.CharField(max_length=13,help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')    
    genre = models.ManyToManyField(Genre,help_text = 'Select Genre of book')
    image = models.CharField(max_length=200,help_text="Enter the image url",null=True)
    description = models.CharField(max_length=500,help_text="Enter the description",null=True)
    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    due_date = models.DateField(null = True)
    
    STATUS = (
        ('R','Reserved'),
        ('A','Available'),
        ('D','Due'),
        ('T','Taken')
    )

    status = models.CharField(max_length = 1,choices = STATUS,default = 'A')

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.book