# Generated by Django 3.1.1 on 2020-09-17 10:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0003_auto_20200917_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='from_who',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='from_by',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d6deadf2-b5ee-4139-bf69-23eeea9ffd96'), unique=True),
        ),
    ]
