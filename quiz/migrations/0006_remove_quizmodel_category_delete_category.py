# Generated by Django 4.1.7 on 2023-03-10 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_quizmodel_description_remove_quizmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
