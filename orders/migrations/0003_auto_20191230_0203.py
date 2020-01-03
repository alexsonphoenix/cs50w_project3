# Generated by Django 2.0.3 on 2019-12-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='dinner_platter',
            field=models.ManyToManyField(blank=True, related_name='dinner_platter_carts', to='orders.Dinner_platter'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pasta',
            field=models.ManyToManyField(blank=True, related_name='pasta_carts', to='orders.Pasta'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='pizza_carts', to='orders.Pizza'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='salad',
            field=models.ManyToManyField(blank=True, related_name='salad_carts', to='orders.Salad'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='sub',
            field=models.ManyToManyField(blank=True, related_name='sub_carts', to='orders.Sub'),
        ),
    ]
