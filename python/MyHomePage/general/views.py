from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import generic
from utils import tweet
from .forms import TweetListForm, MyTweetListForm
from .models import Tweet, TwitterAccessToken
from requests_oauthlib import OAuth1Session

_api = tweet.api


class IndexView(generic.TemplateView):
    template_name = "general/index.html"


class TweetListView(generic.FormView):
    template_name = "general/tweet_list.html"
    form_class = TweetListForm

    def get_context_data(self, **kwargs):
        if 'screen_name' in self.request.GET:
            statuses = _api.GetUserTimeline(screen_name=self.request.GET['screen_name'])
            kwargs['statuses'] = statuses
        return super(TweetListView, self).get_context_data(**kwargs)


class ShowJsonDataView(generic.TemplateView):
    template_name = "general/show_json_data.html"

    def get_context_data(self, **kwargs):
        data = tweet.JsonManager.get_data("data/js/tweets/hoge")
        kwargs['data'] = data[0]
        return super(ShowJsonDataView, self).get_context_data(**kwargs)


class MyTweetListView(generic.ListView, generic.edit.BaseFormView):
    model = Tweet
    paginate_by = 50
    form_class = MyTweetListForm

    def get_template_names(self):
        return "general/my_tweet_list.html"

    def get_queryset(self):
        self.queryset = super(MyTweetListView, self).get_queryset()
        if 'text' in self.request.GET:
            text = self.request.GET['text']
            words = text.split()
            q = Q()
            for word in words:
                q = q & Q(text__icontains=word)
            self.kwargs['text'] = text
            self.queryset = self.queryset.filter(q)
        if 'created_at' in self.request.GET:
            created_at = self.request.GET['created_at']
            self.kwargs['created_at'] = created_at
            if created_at != "":
                self.queryset = self.queryset.filter(created_at=created_at)
        self.kwargs['hit_count'] = self.queryset.count()
        return self.queryset

    def get_context_data(self, **kwargs):
        kwargs.update(self.kwargs)
        return super(MyTweetListView, self).get_context_data(**kwargs)

    def post(self, request):
        if 'delete' in request.POST:
            tweet_id = request.POST['tweet_id']
            # Twitterからツイートを削除
            _api.DestroyStatus(tweet_id)
            # DBからツイートを削除
            Tweet.objects.get(tweet_id=tweet_id).delete()
            return HttpResponseRedirect(reverse("general:my_tweet_list"))

        if 'delete_all' in request.POST:
            print("delete_all excuted!!")
            self.queryset = super(MyTweetListView, self).get_queryset()
            if 'text' in self.request.POST:
                text = self.request.POST['text']
                words = text.split()
                q = Q()
                for word in words:
                    q = q & Q(text__icontains=word)
                self.queryset = self.queryset.filter(q)
            if 'created_at' in self.request.POST:
                created_at = self.request.POST['created_at']
                if created_at != "":
                    self.queryset = self.queryset.filter(created_at=created_at)
            print(self.queryset)
            for t in self.queryset:
                tweet_id = t.tweet_id
                _api.DestroyStatus(tweet_id)
                t.delete()
            return HttpResponseRedirect(reverse("general:my_tweet_list"))


class Authorization(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        oauth_client = OAuth1Session(client_key=tweet.CK,
                                     client_secret=tweet.CS)
        resp = oauth_client.fetch_request_token(tweet.REQUEST_TOKEN_URL)
        url = oauth_client.authorization_url(tweet.AUTHORIZATION_URL)
        self.request.session['request_secret'] = resp.get('oauth_token_secret')
        return url


class TwitterCallBack(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        oauth_client = OAuth1Session(client_key=tweet.CK,
                                     client_secret=tweet.CS,
                                     resource_owner_key=self.request.GET['oauth_token'],
                                     resource_owner_secret=self.request.session['request_secret'],
                                     verifier=self.request.GET['oauth_verifier'])
        resp = oauth_client.fetch_access_token(tweet.ACCESS_TOKEN_URL)
        import datetime
        TwitterAccessToken(key=resp['oauth_token'], secret=resp['oauth_token_secret'],
                           user_id=resp['user_id'], screen_name=resp['screen_name'],
                           x_auth_expires=resp['x_auth_expires'],
                           created_at=datetime.datetime.now()).save()
        return "http://localhost:8000"

