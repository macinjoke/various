from django.db import models


class Tweet(models.Model):
    tweet_id = models.BigIntegerField("ツイートID", unique=True)
    screen_name = models.CharField("ユーザーID", max_length=20)
    text = models.TextField("ツイート内容", max_length=150)
    profile_image_url_https = models.CharField("アイコン画像", max_length=100)
    created_at = models.DateTimeField("投稿日")

    class Meta:
        ordering = ['-created_at']


class TwitterAccessToken(models.Model):
    key = models.CharField("アクセスキー", max_length=110)
    secret = models.CharField("アクセスシークレット", max_length=100)
    user_id = models.CharField("User ID", max_length=20)
    screen_name = models.CharField("Screen name", max_length=100)
    x_auth_expires = models.IntegerField("有効期限")
    created_at = models.DateTimeField("登録日")

    class Meta:
        ordering = ['-created_at']


class LaboEntryCount(models.Model):
    teacher = models.CharField("先生", max_length=20)
    entry_count = models.IntegerField("登録者数")


class LaboRssItemCount(models.Model):
    count = models.IntegerField("登録された回数")
