# Generated by Django 3.0.7 on 2020-06-29 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cmp_reg_imagea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carriera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='upload_files/')),
                ('file_name', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
        ),
    ]
