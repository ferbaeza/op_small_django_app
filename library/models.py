from email.policy import default
import uuid
from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name= models.CharField(max_length=65,default="Literatura", help_text="Pon el nombre del genero")


    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=65)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=255, help_text=f"Sumario de:  {title}")
    isbn = models.CharField("ISBN", max_length=15, help_text="ISBN de 15 caracteres")
    genre = models.ManyToManyField("Genre")

    def __str__(self) -> str:
        return f"{self.title}, {self.author}"

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Id unico uuid4 para este libro")
    book= models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back= models.DateField(null=True, blank=True)

    LOAN_STATUS=(
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Avaiable"),
        ("r", "Reserved"),
        ("s", "Comming soon"),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default="m", help_text="Indica la disponibilidad del libro")

    class Meta:
        ordering=["due_back"]

    def __str__(self) -> str:
        return f"{self.id} --> {self.book.title}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField(null=True, blank=True)
    date_death = models.DateField("Dead",null=True, blank=True)

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])


    def __str__(self) -> str:
        return "%s %s"%(self.first_name, self.last_name)
