# Generated by Django 3.2.4 on 2021-06-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionori',
            name='detail_url',
            field=models.CharField(max_length=500, null=True, verbose_name='详情链接'),
        ),
        migrations.AlterField(
            model_name='positionori',
            name='position_location',
            field=models.CharField(max_length=500, null=True, verbose_name='工作地点'),
        ),
        migrations.AlterField(
            model_name='positionori',
            name='position_skill',
            field=models.CharField(max_length=500, null=True, verbose_name='职位技能'),
        ),
        migrations.AlterField(
            model_name='positionori',
            name='position_welfare',
            field=models.CharField(max_length=500, null=True, verbose_name='职位福利'),
        ),
    ]