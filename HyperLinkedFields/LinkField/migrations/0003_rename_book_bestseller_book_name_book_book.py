# Generated by Django 4.1 on 2022-08-26 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LinkField', '0002_bestseller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestseller',
            old_name='book',
            new_name='book_name',
        ),
        migrations.AddField(
            model_name='book',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LinkField.bestseller'),
        ),
    ]
