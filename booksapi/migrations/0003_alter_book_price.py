# Generated by Django 4.1.1 on 2022-09-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapi', '0002_rename_books_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
