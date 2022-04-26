from rest_framework import serializers

from core.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    """This serializer is used to create the tweet"""

    class Meta:
        model = Tweet
        fields = "__all__"

    def create(self, validated_data):
        instance = Tweet.objects.create(**validated_data)
        return instance
