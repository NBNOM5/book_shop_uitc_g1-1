from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Nomi")
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=40, verbose_name="Ismi")
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    """ Kitoblar uchun yaratilgan 'Book' classi """
    name = models.CharField(max_length=250, verbose_name='Nomi')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name='book_category')
    author = models.ForeignKey( 
        Author, on_delete=models.CASCADE, blank=True, null=True, related_name='book_author')
    description = models.TextField(verbose_name="Ta'rif")
    photo = models.ImageField(
        upload_to='books_photo/%Y/%m/%d/', blank=True, null=True, verbose_name='rasmi')
    # ISBN - kitobning takrorlanmas ID raqami
    isbn = models.PositiveIntegerField(unique=True, verbose_name="ISBN")
    file = models.FileField(upload_to='books_file/%Y/%m/%d/',
                            blank=True, null=True, verbose_name="Fayli")
    audio = models.FileField(
        upload_to='books_audio/%Y/%m/%d/', blank=True, null=True, verbose_name="Audiosi")
    download_count = models.PositiveIntegerField(
        default=0, verbose_name="Yuklab olishlar soni")

    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
