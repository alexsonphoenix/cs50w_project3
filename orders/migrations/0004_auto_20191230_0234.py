# Generated by Django 2.0.3 on 2019-12-30 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191230_0203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='dinner_platter',
            new_name='dinner_platters',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='pasta',
            new_name='pastas',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='pizza',
            new_name='pizzas',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='salad',
            new_name='salads',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='sub',
            new_name='subs',
        ),
    ]
