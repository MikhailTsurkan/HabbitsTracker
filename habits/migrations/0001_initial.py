# Generated by Django 5.0.6 on 2024-05-20 13:40

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(help_text='место, в котором необходимо выполнять привычку', max_length=128,
                                           verbose_name='Место')),
                ('perform_at', models.TimeField(blank=True, default=datetime.datetime(2024, 5, 20, 13, 40, 58, 161558,
                                                                                      tzinfo=datetime.timezone.utc),
                                                help_text='время, когда необходимо выполнять привычку', null=True,
                                                verbose_name='Время')),
                ('action', models.CharField(help_text='действие, которое представляет собой привычка', max_length=256,
                                            verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=False,
                                                    help_text='привычка, которую можно привязать к выполнению полезной привычки',
                                                    verbose_name='Признак приятной привычки')),
                ('periodicity', models.PositiveSmallIntegerField(blank=True, default=1,
                                                                 help_text='периодичность выполнения привычки для напоминания в днях',
                                                                 null=True, verbose_name='Периодичность')),
                ('reward',
                 models.CharField(blank=True, help_text='ем пользователь должен себя вознаградить после выполнения',
                                  max_length=256, null=True, verbose_name='Вознаграждение')),
                ('perform_in', models.DurationField(
                    help_text='время, которое предположительно потратит пользователь на выполнение привычки',
                    verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False,
                                                  help_text='привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки',
                                                  verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True,
                                                    help_text='привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных',
                                                    null=True, on_delete=django.db.models.deletion.CASCADE,
                                                    to='habits.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(help_text='создатель привычки', on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
