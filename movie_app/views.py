from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializer import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status


@api_view(http_method_names=['GET'])
def director_api_view(request):
    director = Director.objects.all()
    data = DirectorSerializer(instance=director, many=True).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)

    data = DirectorSerializer(instance=director).data
    return Response(data=data)


# ///////////////////////////////////////////////////////////////////////

@api_view(http_method_names=['GET'])
def movie_api_view(request):
    movie = Movie.objects.all()
    data = MovieSerializer(instance=movie, many=True).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)

    data = MovieSerializer(instance=movie).data
    return Response(data=data)


# ///////////////////////////////////////////////////////////////////////

@api_view(http_method_names=['GET'])
def review_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(instance=review, many=True).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)

    data = ReviewSerializer(instance=review).data
    return Response(data=data)
