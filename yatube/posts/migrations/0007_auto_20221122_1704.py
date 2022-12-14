# Generated by Django 2.2.16 on 2022-11-22 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.URLField(verbose_name='Ссылка на пост')),
                ('author', models.URLField(verbose_name='Ссылка на автора')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
            ],
            options={
                'verbose_name': 'Коммент',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(blank=True, help_text='Напишите свой комментарий', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.Comment', verbose_name='Комментарий'),
        ),
    ]
