from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
# from genres.models import Genre
# from actors.models import Actor


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True) #calculated field! (campo calculado)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg'] #vai retornar stars__avg que é o padrão que ele usa

        if rate:
            return round(rate, 1)
        
        return None
                      
        # reviews = obj.reviews.all()

        # if reviews:
        #     sum_reviews = 0

        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count, 1)

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('Movies must be realeased after 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resume must have 200 characters at most.')
        return value




# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset=Genre.objects.all(),
#     )
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset=Actor.objects.all(),
#         many=True,
#     )
#     resume = serializers.CharField()