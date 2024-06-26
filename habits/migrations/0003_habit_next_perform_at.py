# Generated by Django 5.0.6 on 2024-05-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('habits', '0002_alter_habit_perform_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='next_perform_at',
            field=models.DateTimeField(default=None,
                                       help_text='время, в которое нужно выполнить привычку в следующий раз',
                                       verbose_name='Время следующего выполнения'),
            preserve_default=False,
        ),
    ]
