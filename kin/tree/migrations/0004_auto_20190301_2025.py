# Generated by Django 2.1.7 on 2019-03-01 20:25

from django.db import migrations, models
import tree.models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20190301_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kin',
            name='yob',
            field=models.SmallIntegerField(null=True, validators=[tree.models.max_year_validator], verbose_name='year of birth'),
        ),
    ]
