from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializer import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status


@api_view(http_method_names=['GET', 'POST'])
def director_create_api_view(request):
    if request.method == 'GET':
        director = Director.objects.annotate(movies_count=Count('movies')).all()
        data = DirectorSerializer(instance=director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get("name")
        director = Director.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED,
                        data={'director_id': director.id})



@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.annotate(movies_count=Count('movies')).get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(instance=director).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ///////////////////////////////////////////////////////////////////////

@api_view(http_method_names=['GET', 'POST'])
def movie_api_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieSerializer(instance=movie, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id,
        )
        return Response(status=status.HTTP_201_CREATED,
                        data={'movie_id':movie.id})
@api_view(http_method_names=['GET'])
def movies_with_reviews_api_view(request):
    movies = Movie.objects.prefetch_related('reviews')
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(instance=movie).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ///////////////////////////////////////////////////////////////////////

@api_view(http_method_names=['GET', 'POST'])
def review_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(instance=review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review =  Review.objects.create(
            text=text,
            movie_id=movie_id,
            stars=stars,
        )
        return Response(status=status.HTTP_201_CREATED,
                        data={'review_id': review.id})


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(instance=review).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
