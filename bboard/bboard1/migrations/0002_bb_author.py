# Generated by Django 3.2.7 on 2021-09-22 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bboard1', '0001_squashed_0004_bb_rubric'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user', verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
