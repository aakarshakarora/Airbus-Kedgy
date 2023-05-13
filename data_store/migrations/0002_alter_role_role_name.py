# Generated by Django 4.1.1 on 2023-05-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('fab_manager', 'Fabricator Manager'), ('sub_assembly_manager', 'Sub Assembly Manager'), ('assembly_manager', 'Assembly Manager'), ('operator', 'Operator')], max_length=50),
        ),
    ]
