from django.conf.urls import url

from . import views

app_name = 'general'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^tweet_list$', views.TweetListView.as_view(), name='tweet_list'),
    # url(r'^show_json_data$', views.ShowJsonDataView.as_view(), name='show_json_data'),
    # url(r'^my_tweet_list$', views.MyTweetListView.as_view(), name='my_tweet_list'),
    url(r'^authorization$', views.Authorization.as_view(), name='authorization$'),
    url(r'^twitter-callback$', views.TwitterCallBack.as_view(), name='twitter_callback'),
]