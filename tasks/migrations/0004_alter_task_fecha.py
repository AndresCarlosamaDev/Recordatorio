# Generated by Django 4.1.7 on 2023-03-12 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_descripcion_alter_task_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 11, 21, 39, 57, 828590)),
        ),
    ]