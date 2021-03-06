# Generated by Django 3.0.3 on 2020-03-28 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
        ('product', '0010_auto_20200325_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRODImage',
            field=models.ImageField(blank=True, null=True, upload_to='prodcut/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRODBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.Brand', verbose_name='Product Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRODCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Product Category'),
        ),
    ]
