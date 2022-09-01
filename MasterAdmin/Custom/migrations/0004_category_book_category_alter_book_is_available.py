# Generated by Django 4.1 on 2022-08-24 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Custom', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='book_category',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='is_available',
            field=models.BooleanField(help_text='Is the book available to buy?'),
        ),
    ]