# Generated by Django 4.0.4 on 2022-05-18 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledayperiod',
            name='schedule_day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='day_app.scheduleday'),
            preserve_default=False,
        ),
    ]
