# Generated by Django 4.2 on 2025-02-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tag_alter_article_abstract_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
    ]
