# Generated by Django 2.2.1 on 2019-07-24 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_tweet_origin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='sentiment_blob_nbc',
            new_name='sentiment_nbc',
        ),
    ]