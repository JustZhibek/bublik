# Generated by Django 4.1.7 on 2023-02-19 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lost',
            name='created_date',
        ),
        migrations.AddField(
            model_name='lost',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='lost',
            name='types',
            field=models.CharField(choices=[('Fantasy', 'Фэнтези'), ('Romance novel', 'Любовный роман'), ('Short stories', 'Короткие истории'), ('Western', 'Вэстерн')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lost',
            name='description',
            field=models.TextField(verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='lost',
            name='title',
            field=models.CharField(max_length=190, verbose_name='Название книги'),
        ),
    ]
