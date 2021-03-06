# Generated by Django 3.0 on 2020-01-13 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_auto_20200113_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('f_address', models.CharField(max_length=100)),
                ('f_gender', models.CharField(max_length=10)),
                ('f_mobile', models.IntegerField()),
                ('f_email', models.CharField(blank=True, max_length=50, null=True)),
                ('f_designation', models.CharField(default='', max_length=20)),
                ('f_dob', models.DateField()),
                ('f_joiningdate', models.DateField()),
                ('f_bloodgroup', models.CharField(default='', max_length=10)),
                ('f_batch', models.CharField(max_length=10)),
                ('f_qualfication', models.CharField(max_length=10)),
                ('f_password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'facultydetails',
            },
        ),
    ]
