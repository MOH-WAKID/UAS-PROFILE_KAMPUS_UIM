# Generated by Django 4.2.6 on 2024-01-02 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visimisi',
            name='sejarahkampus_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uim.sejarahkampus'),
        ),
    ]
