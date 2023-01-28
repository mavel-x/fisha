# Generated by Django 4.1.5 on 2023-01-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_placeimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='lon',
            new_name='lng',
        ),
        migrations.AddField(
            model_name='placeimage',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='порядковый номер'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='картинка'),
        ),
        migrations.AlterUniqueTogether(
            name='placeimage',
            unique_together={('place', 'position')},
        ),
    ]