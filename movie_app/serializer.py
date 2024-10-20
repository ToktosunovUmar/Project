from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=5, max_length=255)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField(min_value=1, max_value=100)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Director.DoesNotExist:
            raise ValidationError("Director not exist")
        return movie_id


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class MovieWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'id title description duration director reviews'.split()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError("Director not exist")
        return director_id
