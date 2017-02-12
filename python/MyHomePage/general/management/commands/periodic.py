# coding: utf-8

from django.core.management.base import BaseCommand
from utils import tweet
from ...models import TwitterAccessToken
import twitter
import datetime

_api = tweet.api

class Command(BaseCommand):
    help = 'cronから呼ばれる定期処理です'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)
    #     parser.add_argument(
    #         '--delete',
    #         action='store_true',
    #         dest='delete',
    #         default=False,
    #         help='Delete poll instead of closing it',
    #     )

    def handle(self, *args, **options):
        # if options['poll_id']:
        #     print('poll_id: %s' % options['poll_id'])
        # if options['delete']:
        #     print('delete !!')

        print("START periodic [%s]" % datetime.datetime.now())
        tokens = TwitterAccessToken.objects.all()
        for token in tokens:
            api = twitter.Api(consumer_key=tweet.CK, consumer_secret=tweet.CS,
                              access_token_key=token.key, access_token_secret=token.secret)
            statuses = api.GetFavorites()
            print("[%s] favorite list searching" % token.screen_name)
            for status in statuses:
                if str(status.user.id) == token.user_id:
                    api.DestroyStatus(status.id)
                    print("Delete tweet of following text!!")
                    print(status.text)
        print("END periodic")

