# Generated by Django 3.1.7 on 2021-04-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210402_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitter_data',
            name='followers_count',
        ),
        migrations.AddField(
            model_name='twitter_data',
            name='follower_count',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='created_at',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='friend_count',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='last_tweet',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='last_tweet_time',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='screen_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='verified',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
