# Generated by Django 5.1.2 on 2024-12-07 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_new_tags_post_tags_alter_tag_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
    ]
