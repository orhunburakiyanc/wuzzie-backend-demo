# Generated by Django 5.0.6 on 2024-07-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wuzzie', '0002_alter_item_item_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_types',
            field=models.CharField(choices=[('bottom', 'Bottom'), ('jewelry', 'Jewelry'), ('top', 'Top'), ('eyewear', 'Eyewear'), ('footwear', 'Footwear'), ('outerwear', 'Outerwear')], max_length=10),
        ),
    ]
