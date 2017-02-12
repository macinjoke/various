# coding: utf-8

from django.core.management.base import BaseCommand
from ...models import LaboEntryCount, LaboRssItemCount
from utils import tweet
import requests
import xmltodict
from bs4 import BeautifulSoup
from local_setting import labo
import random

random_text_list = ["(・∀・)", "(^^ゞ", "(*_*)", "(T_T)", "(-_-;)", "(・ω<)",
                    "＼(^o^)／", "(^_-)-☆", "(・o・)", "(*´∀｀)", "(・へ・)"]

_api = tweet.api


class Command(BaseCommand):
    RSS_URL = labo.RSS_URL
    HTML_URL = labo.HTML_URL
    USER = labo.USER
    PASS = labo.PASS

    TEACHERS_CAPACITY = {
        '絹川': 10, '小山': 10, '矢島': 10, '齊藤': 10, '小坂': 10,
        '中島': 10, '高橋': 10, '鉄谷': 10, '川澄': 10, '増田': 10,
        '猪俣・佐々木': 10, '岩井': 10, '竜田': 2, '山田': 2,
        '柿崎': 2, '森谷': 2, '井ノ上': 2, '学科外(系列等)': 10
    }

    def handle(self, *args, **options):
        text = self.fetch_rss_text(self.RSS_URL, self.USER, self.PASS)
        data = xmltodict.parse(text)
        items = data['rdf:RDF']['item']
        present_count = len(items)
        rss_item_model = LaboRssItemCount.objects.get(id=1)
        previous_count = rss_item_model.count
        if present_count != previous_count:
            print("[更新あり] RSS entry count : %s" % present_count)
            rss_item_model.count = present_count
            rss_item_model.save()
            self.tweet_logic()
        else:
            print("[更新なし] RSS entry count : %s" % present_count)
            # print("が試験的にtweet_logic()を呼ぶ")
            # self.tweet_logic()

    def tweet_logic(self):
        text = self.fetch_html_text(self.HTML_URL, self.USER, self.PASS)
        soup = BeautifulSoup(text, "html.parser")
        table = soup.find("table")
        trs = table.find_all("tr")

        # initialize present entry_count
        entry_count = {}
        for teacher in self.TEACHERS_CAPACITY.keys():
            entry_count[teacher] = 0

        # input present entry count
        for key, tr in enumerate(trs):
            if key == 0:  # skip th tag
                continue
            teacher = tr.find_next().find_next().find_next().get_text()
            if teacher in self.TEACHERS_CAPACITY.keys():
                entry_count[teacher] += 1

        # input previous entry count
        models = LaboEntryCount.objects.all()
        pre_entry_count = {}
        for model in models:
            pre_entry_count[model.teacher] = model.entry_count

        if pre_entry_count == entry_count:
            print("[更新なし]")
        else:
            print("[更新あり]")
            self.compare(pre_entry_count, entry_count, models)

    def compare(self, previous, present, models):
        for key, value in previous.items():
            print("%s : %s" % (key, value))
        for key, value in present.items():
            print("%s : %s" % (key, value))

        for key, value in present.items():
            if value > previous[key]:
                print("[多くなった　] %s " % key)
                model = models.get(teacher=key)
                model.entry_count = value
                model.save()
                self.tweet(key, previous[key], value, up=True)
            elif value < previous[key]:
                print("[少なくなった] %s" % key)
                model = models.get(teacher=key)
                model.entry_count = value
                model.save()
                self.tweet(key, previous[key], value, up=False)
            else:
                print("[変化なし　　] %s" % key)

    def tweet(self, teacher, previous_count, present_count, up):
        if up:
            up_or_down_text = "増えました"
        else:
            up_or_down_text = "減りました"
        fill = ""; empty = ""; excess = ""
        if self.TEACHERS_CAPACITY[teacher] >= present_count:
            for i in range(self.TEACHERS_CAPACITY[teacher]):
                if i < present_count:
                    fill += "■"
                else:
                    empty += "❏"
        else:
            for i in range(present_count):
                if i < self.TEACHERS_CAPACITY[teacher]:
                    fill += "■"
                else:
                    excess += "超"
        graph = fill + empty + excess

        tweet_text = "%s が%s人から%s人に%s。\n%s/%s  %s\n %s" \
                     % (teacher, previous_count, present_count,
                        up_or_down_text, present_count,
                        Command.TEACHERS_CAPACITY[teacher],
                        random.choice(random_text_list), graph)
        _api.PostUpdate(tweet_text)

    @staticmethod
    def fetch_rss_text(url, user, password):
        auth = (user, password)
        r = requests.post(url, auth=auth)
        r.encoding = 'UTF-8'
        return r.text

    @staticmethod
    def fetch_html_text(url, user, password):
        payload = {'id': user,
                   'code': password,
                   'func': 'authByRadius'}
        r = requests.post(url, payload)
        return r.text



