# Generated by Django 4.2 on 2023-04-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('op_type', models.CharField(choices=[('addition', 'addition'), ('subtraction', 'subtraction'), ('multiplication', 'multiplication'), ('division', 'division'), ('square_root', 'square_root'), ('random_string', 'random_string')], max_length=30)),
            ],
        ),
    ]
