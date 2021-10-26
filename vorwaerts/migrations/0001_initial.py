# Generated by Django 3.2.8 on 2021-10-26 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassifiedAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewspaperPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=100)),
                ('publish_date', models.DateField(null=True)),
                ('issue_number', models.IntegerField(null=True)),
                ('page_number', models.IntegerField(null=True)),
                ('width', models.CharField(max_length=5, null=True)),
                ('height', models.CharField(max_length=5, null=True)),
            ],
            options={
                'ordering': ['publish_date', 'page_number'],
            },
        ),
        migrations.AddIndex(
            model_name='newspaperpage',
            index=models.Index(fields=['publish_date', 'page_number'], name='vorwaerts_n_publish_4e683d_idx'),
        ),
        migrations.AddField(
            model_name='classifiedad',
            name='newspaper_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', related_query_name='advertisment', to='vorwaerts.newspaperpage'),
        ),
    ]
