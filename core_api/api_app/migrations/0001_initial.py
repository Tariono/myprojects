# Generated by Django 2.1.7 on 2019-03-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key_word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(db_index=True, max_length=100)),
                ('videos', models.CharField(blank=True, max_length=100000, null=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
