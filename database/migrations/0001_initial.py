# Generated by Django 4.0.5 on 2022-07-03 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contest_ID', models.CharField(default='Contest 1', max_length=100)),
                ('Contest_name', models.CharField(default='Contest 1', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Problem_ID', models.CharField(max_length=100)),
                ('Problem_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=50)),
                ('solved_status', models.CharField(default='Unsolved', max_length=10)),
                ('Score', models.FloatField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.contest')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.FloatField(default=0)),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='test_case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Input', models.CharField(max_length=100)),
                ('Output', models.CharField(max_length=100)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.problem')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Verdict', models.CharField(default='NA', max_length=20)),
                ('Timestamp', models.DateTimeField(verbose_name='submitted at')),
                ('runtime', models.CharField(max_length=2)),
                ('Userp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.users')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.problem')),
            ],
        ),
    ]
