from django.shortcuts import render
from pipenv.cli.options import categories_option
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Topic, Post, Category
from .serializers import TopicSerializer, PostModelSerializer, CategoryModelSerializer


@api_view(['GET'])
def topic_list(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_post_list(request):
    posts = Post.objects.filter(created_by=request.user)
    serializer = PostModelSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def topic_search_by_name(request, phrase):
    topics = Topic.objects.filter(name__icontains=phrase)
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_search_by_name(request, phrase):
    categories = Category.objects.filter(name__icontains=phrase)
    serializer = CategoryModelSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_search_by_name(request, phrase):
    posts = Post.objects.filter(name__icontains=phrase)
    serializer = PostModelSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def topic_and_category_search_by_name(request, phrase):
    topics = Topic.objects.filter(name__icontains=phrase)
    categories = Category.objects.filter(name__icontains=phrase)
    topic_serializer = TopicSerializer(topics, many=True)
    category_serializer = CategoryModelSerializer(categories, many=True)

    my_data = {}
    my_data['topics'] = topic_serializer.data
    my_data['categories'] = category_serializer.data

    return Response(my_data)

@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Topic
    :return: Response (with status and/or object/s data)
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Topic.
    """
    if request.method == 'GET':
        topic = Topic.objects.get(pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Topic
    :return: Response (with status and/or object/s data)
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Category.
    """
    if request.method == 'GET':
        category = Category.objects.get(pk=pk)
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Topic
    :return: Response (with status and/or object/s data)
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Category.
    """
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        serializer = PostModelSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostModelSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def topic_create(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def category_create(request):
    serializer = CategoryModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_create(request):
    serializer = PostModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)