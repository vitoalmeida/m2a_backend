# Generated by Django 3.2.7 on 2022-06-26 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faturamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ano', models.DateField()),
                ('valor', models.FloatField()),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
                ('empresa_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresamaster')),
            ],
        ),
    ]
