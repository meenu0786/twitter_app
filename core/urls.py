from django.urls import path

from core.views import CreateTweetView, GetAllTweetListView

app_name = "core"

urlpatterns = [
    path("create_tweet/", CreateTweetView.as_view(), name="create_tweet"),
    path("get_tweet_list/", GetAllTweetListView.as_view(), name="get_tweet_list"),
]
