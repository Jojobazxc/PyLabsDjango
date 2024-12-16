from django.db import models
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        help_text="Введите имя автора",
        verbose_name="Имя автора"
    )
    last_name = models.CharField(
        max_length=100,
        help_text="Введите фамилию автора",
        verbose_name="Фамилия автора"
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        help_text="Введите дату рождения",
        verbose_name="Дата рождения"
    )
    date_of_death = models.DateField(
        blank=True,
        null=True,
        help_text="Введите дату смерти",
        verbose_name="Дата смерти"
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Введите жанр книги",
        verbose_name="Жанр книги"
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    lang = models.CharField(
        max_length=20,
        help_text="Введите язык книги",
        verbose_name="Язык книги"
    )

    def __str__(self):
        return self.lang


class Status(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Введите статус экземпляра книги",
        verbose_name="Статус экземпляра книги"
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Введите название книги",
        verbose_name="Название книги"
    )
    summary = models.TextField(
        max_length=1000,
        help_text="Введите краткое описание книги",
        verbose_name="Аннотация книги"
    )
    isbn = models.CharField(
        max_length=13,
        help_text="Должно содержать 13 символов",
        verbose_name="ISBN книги"
    )
    author = models.ManyToManyField(
        'Author',
        help_text="Выберите автора книги",
        verbose_name="Автор книги",
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        help_text="Выберите жанр для книги",
        verbose_name="Жанр книги",
        null=True
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
        help_text="Выберите язык книги",
        verbose_name="Язык книги",
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'


class BookInstance(models.Model):
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        null=True
    )
    imprint = models.CharField(
        max_length=200,
        help_text="Введите издательство и год выпуска",
        verbose_name="Издательство"
    )
    due_back = models.DateField(
        blank=True,
        null=True,
        help_text="Введите конец срока статуса",
        verbose_name="Дата окончания статуса"
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
        help_text="Изменить состояние экземпляра",
        verbose_name="Статус экземпляра книги",
        null=True
    )

    def __str__(self):
        return f"{self.book.title} ({self.status})"