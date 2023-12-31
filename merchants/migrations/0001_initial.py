# Generated by Django 4.2.7 on 2023-11-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated At')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Merchant',
                'verbose_name_plural': 'Merchants',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=255)),
                ('merchant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='merchants.merchant')),
            ],
            options={
                'verbose_name': 'User Info',
                'verbose_name_plural': 'User Info',
            },
        ),
        migrations.CreateModel(
            name='MerchantToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated At')),
                ('access_token', models.CharField(max_length=255)),
                ('refresh_token', models.CharField(max_length=255)),
                ('expires', models.DateField()),
                ('merchant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to='merchants.merchant')),
            ],
            options={
                'verbose_name': 'Merchant Token',
                'verbose_name_plural': 'Merchant Tokens',
            },
        ),
        migrations.CreateModel(
            name='MerchantSpecialOffer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated At')),
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Special Offer Message')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_offers', to='merchants.merchant')),
            ],
            options={
                'verbose_name': 'Merchant Special Offer',
                'verbose_name_plural': 'Merchant Special Offers',
            },
        ),
        migrations.CreateModel(
            name='MerchantBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated At')),
                ('image', models.ImageField(upload_to='merchant/banners')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='merchants.merchant')),
            ],
            options={
                'verbose_name': 'Merchant Banner',
                'verbose_name_plural': 'Merchant Banners',
            },
        ),
    ]
