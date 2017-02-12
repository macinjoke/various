# coding: utf-8

from django.core.management.base import BaseCommand
from general.models import Tweet
from utils import tweet
import os
import time


class Command(BaseCommand):
    __js_path = 'data/js/'
    __tweets_path = __js_path+'tweets/'
    __tweets_files = os.listdir(__tweets_path)

    def handle(self, *args, **options):
        print("savetweet command started!!")
        files = map(lambda file: self.__tweets_path+file, self.__tweets_files)
        parser = tweet.JsonManager()
        data = parser.get_data(*files)
        results = []
        for files in data:
            for d in files:
                spt = time.strptime(d['created_at'], '%Y-%m-%d %H:%M:%S +0000')
                results.append({
                    'id': d['id'],
                    'screen_name': d['user']['screen_name'],
                    'text': d['text'],
                    'profile_image_url_https': d['user']['profile_image_url_https'],
                    'created_at': time.strftime('%Y-%m-%d %H:%M:%S', spt)
                })
        for r in results:
            Tweet(tweet_id=r['id'], screen_name=r['screen_name'],text=r['text'],
                  profile_image_url_https=r['profile_image_url_https'],
                  created_at=r['created_at']).save()
        print("successfully saved to DB")



