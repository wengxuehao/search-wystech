# Generated by Django 2.2 on 2019-04-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recognize_model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='识别种类id')),
                ('name', models.CharField(default='', max_length=10, verbose_name='识别种类名称')),
                ('description', models.CharField(max_length=50, verbose_name='识别种类描述')),
            ],
            options={
                'verbose_name': '识别种类模型',
                'verbose_name_plural': '识别种类模型',
            },
        ),
    ]
