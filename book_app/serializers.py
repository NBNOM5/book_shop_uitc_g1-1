from .models import Category, Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    # author_id = serializers.IntegerField(source='author.id')
    # author_status = serializers.BooleanField(source='author.status')
    author_name = serializers.CharField(source='author.full_name')
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'photo', 'file', 'audio',
                  'download_count', 'author_name', 'category_name', 'isbn')

class CategorySerializer(serializers.ModelSerializer):
    book_category = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'book_category')
        # fields = ('__all__')

class AuthorSerializer(serializers.ModelSerializer):
    book_author = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'full_name', 'book_author')

