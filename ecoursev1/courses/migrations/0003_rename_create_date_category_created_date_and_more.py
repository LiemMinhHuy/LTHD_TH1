# Generated by Django 5.0.3 on 2024-03-05 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_active_category_create_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='update_date',
            new_name='updated_date',
        ),
    ]
