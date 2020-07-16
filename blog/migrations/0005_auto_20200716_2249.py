# Generated by Django 3.0.8 on 2020-07-16 22:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='date_upd',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categorie',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorie',
            name='date_upd',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='categorie',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentaire',
            name='date_upd',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='date_upd',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
