# Generated by Django 3.1.5 on 2021-05-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniMart', '0003_auto_20210519_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tag_name',
        ),
        migrations.AddField(
            model_name='product',
            name='tag_name',
            field=models.ManyToManyField(to='MiniMart.Tags'),
        ),
    ]