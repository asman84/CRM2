# Generated by Django 3.2.4 on 2021-06-24 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_category_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]