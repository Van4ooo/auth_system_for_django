# Generated by Django 4.0.5 on 2022-06-29 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='data_of_comment',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
