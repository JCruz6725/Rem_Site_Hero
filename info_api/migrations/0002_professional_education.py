# Generated by Django 4.0 on 2022-06-15 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('time_at', models.CharField(max_length=32)),
                ('title_of_project', models.CharField(max_length=32)),
                ('tech_used', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=1024)),
                ('account_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_api.account')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('degree', models.CharField(max_length=128)),
                ('time_at', models.CharField(max_length=32)),
                ('account_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_api.account')),
            ],
        ),
    ]
