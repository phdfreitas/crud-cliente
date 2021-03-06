# Generated by Django 3.1.5 on 2021-01-23 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('data_cadastro',),
            },
        ),
    ]
