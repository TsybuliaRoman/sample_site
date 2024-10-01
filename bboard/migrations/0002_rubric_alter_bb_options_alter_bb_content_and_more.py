# Generated by Django 4.2.16 on 2024-10-01 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Rubric',
                'verbose_name_plural': 'Rubrics',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Announcement', 'verbose_name_plural': 'Announcements'},
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Staff'),
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Rubric'),
        ),
    ]
