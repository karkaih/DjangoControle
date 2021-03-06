# Generated by Django 4.0.4 on 2022-05-08 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('code', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=10, null=True)),
                ('prenom', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('numero', models.IntegerField(max_length=100)),
                ('date_creation', models.DateField()),
                ('solde', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karkaih_achraf.client')),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('numOperation', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('dateOperation', models.DateField()),
                ('montant', models.FloatField()),
                ('client_op', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karkaih_achraf.client')),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karkaih_achraf.compte')),
            ],
        ),
    ]
