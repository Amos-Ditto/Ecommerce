# Generated by Django 3.2.12 on 2022-03-16 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220315_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('code', models.FloatField()),
                ('describtion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.AlterModelOptions(
            name='seller_details',
            options={'verbose_name': 'Seller Details', 'verbose_name_plural': 'Seller Details'},
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('describtion', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='products')),
                ('price', models.FloatField()),
                ('stock', models.BooleanField(default=True)),
                ('premium', models.BooleanField(default=False)),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.seller_details')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
        ),
    ]