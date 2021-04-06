# Generated by Django 3.1.7 on 2021-03-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_proprietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valo_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valo_mes', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]