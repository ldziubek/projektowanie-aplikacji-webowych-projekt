from django.shortcuts import render
from pipenv.cli.options import categories_option
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category, Topic, Tag, Post, Page
from .serializers import CategoryModelSerializer, TopicSerializer, TagModelSerializer, PostModelSerializer, PageModelSerializer

# Listy obiektów
@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def topic_list(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def tag_list(request):
    if request.method == 'GET':
        categories = Tag.objects.all()
        serializer = TagModelSerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def page_list(request):
    if request.method == 'GET':
        posts = Page.objects.all()
        serializer = PageModelSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_post_list(request):
    posts = Post.objects.filter(created_by=request.user)
    serializer = PostModelSerializer(posts, many=True)
    return Response(serializer.data)


# Wyszukiwarki obiektów
@api_view(['GET'])
def category_search_by_name(request, phrase):
    categories = Category.objects.filter(name__icontains=phrase)
    serializer = CategoryModelSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def topic_search_by_name(request, phrase):
    topics = Topic.objects.filter(name__icontains=phrase)
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tag_search_by_name(request, phrase):
    categories = Tag.objects.filter(name__icontains=phrase)
    serializer = TagModelSerializer(tags, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_search_by_name(request, phrase):
    posts = Post.objects.filter(title__icontains=phrase)
    serializer = PostModelSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def page_search_by_name(request, phrase):
    pages = Page.objects.filter(title__icontains=phrase)
    serializer = PageModelSerializer(pages, many=True)
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

# Szczegóły obiektów
@api_view(['GET'])
def category_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Category
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


@api_view(['GET'])
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


@api_view(['GET'])
def tag_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Tag
    :return: Response (with status and/or object/s data)
    """
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Tag.
    """
    if request.method == 'GET':
        category = Tag.objects.get(pk=pk)
        serializer = TagModelSerializer(tag)
        return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Post
    :return: Response (with status and/or object/s data)
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Post.
    """
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        serializer = PostModelSerializer(post)
        return Response(serializer.data)


@api_view(['GET'])
def page_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Page
    :return: Response (with status and/or object/s data)
    """
    try:
        page = Page.objects.get(pk=pk)
    except Page.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Page.
    """
    if request.method == 'GET':
        page = Page.objects.get(pk=pk)
        serializer = PageModelSerializer(page)
        return Response(serializer.data)


# Aktualizacja i kasowanie
@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_update_delete(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Category
    :return: Response (with status and/or object/s data)
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def topic_update_delete(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Topic
    :return: Response (with status and/or object/s data)
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def tag_update_delete(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Tag
    :return: Response (with status and/or object/s data)
    """
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TagModelSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_update_delete(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Post
    :return: Response (with status and/or object/s data)
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostModelSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def page_update_delete(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Page
    :return: Response (with status and/or object/s data)
    """
    try:
        page = Page.objects.get(pk=pk)
    except Page.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PageModelSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Tworzenie obiektów
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_create(request):
    serializer = CategoryModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def topic_create(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def tag_create(request):
    serializer = TagModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_create(request):
    serializer = PostModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def page_create(request):
    serializer = PageModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Dodatkowe endpointy
@api_view(['GET'])
def tag_post_list(request, tag_name):
    if request.method == 'GET':
        posts = Post.objects.filter(tags__name__icontains=tag_name)
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def topic_post_list(request, topic_name):
    if request.method == 'GET':
        posts = Post.objects.filter(topic__name__icontains=topic_name)
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)