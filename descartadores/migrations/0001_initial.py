# Generated by Django 4.2.1 on 2023-09-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descartadores',
            fields=[
                ('nome', models.CharField(default='-', max_length=30)),
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='-', max_length=30)),
                ('endereco', models.CharField(default='-', max_length=30)),
            ],
        ),
    ]
