# Generated by Django 5.0.6 on 2024-05-23 20:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('habits', '0004_alter_habit_next_perform_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'ordering': ['-id'], 'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
    ]