# Generated by Django 3.2.9 on 2021-12-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcomment', '0004_alter_postcomment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='post_id',
            field=models.CharField(default=13, max_length=200),
            preserve_default=False,
        ),
    ]