from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.models import Tweet
from core.serializers import TweetSerializer


class CreateTweetView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TweetSerializer
    __doc__ = """ This api is used to create the a new tweet"""


class GetAllTweetListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TweetSerializer
    __doc__ = """
            This api is used for returning all the tweets
            query_params sort_by:name/time
            """

    def get_queryset(self):
        queryset = Tweet.objects.all()
        sort_by = self.request.GET.get("sort_by")
        if sort_by:
            queryset = queryset.order_by(sort_by)
        return queryset
