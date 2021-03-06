# Generated by Django 3.1 on 2020-10-29 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='attachments',
            field=models.FileField(upload_to='Attachments/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='MultipleFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachments', models.FileField(upload_to='Attachments/%Y/%m/%d')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactapp.contactus')),
            ],
        ),
    ]
