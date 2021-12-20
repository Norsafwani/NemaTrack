# Generated by Django 4.0 on 2021-12-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0004_delete_trackappdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devui', models.CharField(max_length=255)),
                ('app_key', models.CharField(max_length=255)),
                ('ship_date_received', models.DateTimeField()),
                ('site_install_date', models.DateTimeField()),
                ('date_deliver', models.DateTimeField()),
                ('lightsol_name', models.CharField(max_length=255)),
                ('license_active_date', models.DateTimeField()),
                ('license_expired_date', models.DateTimeField()),
                ('contractor_name', models.CharField(max_length=255)),
                ('end_client_name', models.CharField(max_length=255)),
                ('project_tender_name', models.CharField(max_length=255)),
                ('do_number', models.DateTimeField()),
                ('remarks', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'nema',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Returnformnema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateuninstall', models.DateTimeField()),
                ('datedetect', models.DateTimeField()),
                ('proof_describe', models.CharField(max_length=255)),
                ('no_siri', models.CharField(db_column='No_Siri', max_length=255)),
                ('pdf_proof', models.TextField()),
                ('image_proof', models.TextField()),
            ],
            options={
                'db_table': 'returnformnema',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Nema2',
        ),
        migrations.DeleteModel(
            name='Nemareturnform',
        ),
    ]
