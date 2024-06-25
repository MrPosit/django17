from django.db import models

class Book(models.Model):
    class Genre(models.TextChoices):
        ROMAN = 'Roman', 'Роман'
        FANTASY = 'Fantasy', 'Фэнтези'
        MYSTERY = 'Mystery', 'Детектив'
        SCIFI = 'Sci-Fi', 'Научная фантастика'
        NONFICTION = 'Non-fiction', 'Нон-фикшн'

    title = models.CharField(max_length=200, verbose_name='Название')  
    description = models.TextField(verbose_name='Описание')  
    author = models.CharField(max_length=100, verbose_name='Автор')  
    published_year = models.IntegerField(verbose_name='Год публикации') 
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    genre = models.CharField(max_length=50, choices=Genre.choices, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.title} - {self.description[:30]}... - ${self.price}"
