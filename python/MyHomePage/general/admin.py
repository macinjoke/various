from django.contrib import admin
from .models import Tweet, TwitterAccessToken, LaboRssItemCount, LaboEntryCount


class TweetAdmin(admin.ModelAdmin):
    list_display = ('tweet_id', 'screen_name', 'text')
    list_display_links = ('tweet_id', 'screen_name', 'text')
admin.site.register(Tweet, TweetAdmin)


class TwitterAccessTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'secret', 'created_at')
admin.site.register(TwitterAccessToken, TwitterAccessTokenAdmin)


class LaboEntryCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'entry_count')
admin.site.register(LaboEntryCount, LaboEntryCountAdmin)


class LaboRssItemCountAdmin(admin.ModelAdmin):
    list_display = ('count',)
admin.site.register(LaboRssItemCount, LaboRssItemCountAdmin)
