# Generated by Django 5.2 on 2025-06-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('category', models.TextField(max_length=100, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
                'ordering': ['id'],
            },
        ),
    ]
