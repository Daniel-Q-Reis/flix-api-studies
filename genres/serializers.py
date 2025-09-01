from rest_framework import serializers

from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"  # you could have chose the one u want ex: ('id', 'name',)
