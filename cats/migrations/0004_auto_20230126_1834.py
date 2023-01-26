# Generated by Django 3.2 on 2023-01-26 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20230125_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Черный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешаный')], max_length=16),
        ),
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='cats.owner'),
        ),
    ]