# Generated by Django 3.1.5 on 2021-05-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniMart', '0013_auto_20210526_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='<django.db.models.fields.related.OneToOneField>', max_length=50, null=True),
        ),
    ]