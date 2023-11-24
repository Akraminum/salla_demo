# Generated by Django 4.2.6 on 2023-11-21 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sort_order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('visible', 'Visible'), ('hidden', 'Hidden')], default='hidden', max_length=10)),
                ('update_at', models.DateTimeField()),
                ('metadata_title', models.CharField(blank=True, max_length=255, null=True)),
                ('metadata_description', models.TextField(blank=True, null=True)),
                ('metadata_url', models.CharField(blank=True, max_length=255, null=True)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='merchants.merchant', verbose_name='Merchant')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='category.category')),
            ],
        ),
    ]
