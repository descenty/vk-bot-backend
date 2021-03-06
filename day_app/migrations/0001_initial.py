# Generated by Django 4.0.4 on 2022-05-19 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataLastUpdate',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=90)),
                ('form', models.CharField(blank=True, max_length=10, null=True)),
                ('audience_name', models.CharField(blank=True, max_length=10, null=True)),
                ('schedule_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day_app.scheduleday')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='day_app.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day_app.studygroup')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day_app.studygroup')),
            ],
        ),
        migrations.AddField(
            model_name='scheduleday',
            name='schedule_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day_app.scheduleweek'),
        ),
    ]
