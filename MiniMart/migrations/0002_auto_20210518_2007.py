# Generated by Django 3.1.5 on 2021-05-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniMart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Snack', 'Snack'), ('FastFood', 'FastFood'), ('Drink', 'Drink')], max_length=254, null=True),
        ),
    ]
