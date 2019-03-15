from django.db import models
from django.urls import reverse
# from django.utils.text import slugify

class Book(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    url_name = models.URLField(max_length=200)
    # slugs = models.SlugField()
    created_at = models.DateField(auto_now_add=True)
    

    # Metadata
    class Meta: 
        ordering = ['-created_at']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the string representation of book object (in Admin site etc.)."""
        return self.title


class Author(models.Model):    
    name = models.CharField(max_length=200)
