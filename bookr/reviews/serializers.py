#  serializers.py
#  serializing our data converts python attributes into JSON, which our front-end can read.
#  refer to api_views.py

from rest_framework import serializers
from .models import BookContributor


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()
    website = serializers.URLField()
    email = serializers.EmailField()


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    publication_date = serializers.DateField()
    isbn = serializers.CharField()
    publisher = PublisherSerializer()


class ContributionSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookContributor
        fields = ['book', 'role']
