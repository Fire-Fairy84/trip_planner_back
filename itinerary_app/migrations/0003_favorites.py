# Generated by Django 5.1 on 2024-08-27 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary_app', '0002_itinerarydetails'),
        ('user_app', '0002_user_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_date', models.DateTimeField(auto_now_add=True)),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='itinerary_app.itinerary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='user_app.user')),
            ],
            options={
                'unique_together': {('user', 'itinerary')},
            },
        ),
    ]
