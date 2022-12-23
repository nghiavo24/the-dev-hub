# Generated by Django 4.1.4 on 2022-12-23 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('the_dev_hub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('applied', models.DateField()),
                ('hiring_manager', models.CharField(blank=True, max_length=50, null=True)),
                ('compensation', models.IntegerField(blank=True, null=True)),
                ('work_site', models.CharField(default='N/A', max_length=50)),
                ('location', models.CharField(default='N/A', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='the_dev_hub.application')),
            ],
        ),
    ]