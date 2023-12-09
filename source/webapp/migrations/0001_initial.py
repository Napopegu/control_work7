# Generated by Django 5.0 on 2023-12-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя автора записи')),
                ('author_mail', models.EmailField(max_length=100, verbose_name='Почта автора записи')),
                ('text', models.TextField(max_length=200, verbose_name='Текст записи')),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('date_edit', models.DateTimeField(auto_now=True, verbose_name='время редактирования')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Блокировано')], default='active', max_length=25, verbose_name='Статус')),
            ],
        ),
    ]
