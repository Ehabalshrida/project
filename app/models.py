from django.db import models
from django.urls import reverse
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(unique=True)   
    age = models.IntegerField()
    number = models.IntegerField(default='0', validators=[
            MinValueValidator(0),
            MaxValueValidator(9999999999)
        ])
    
    def __str__(self):
     return f"{self.first_name} {self.last_name} ({self.age})"
    # This method returns a string representation of the User object, which is useful for displaying in the Django admin interface and other places where the object is represented as a string.
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users_List'
        ordering = ['-age']  # Order by age descending
        unique_together = ('first_name', 'last_name')  # Ensure unique combination of first and last name
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Language(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    summery = models.TextField()
    isbn = models.CharField('ISBN',max_length=13, unique=True)
    img= models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author} )"
    
    def get_absolute_url(self):
        return reverse('book-details', kwargs={'pk': self.pk})
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors_List'
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f"{self.last_name} - {self.first_name}"
    
    def get_absolute_url(self):
        return reverse('author-details', kwargs={'pk': self.pk})
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across the library")
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    
    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return f"{self.id} - ({self.book.title})"