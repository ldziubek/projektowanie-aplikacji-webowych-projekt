from rest_framework import serializers
from .models import Topic, Category, Post


class TopicSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=60)
    created = serializers.DateTimeField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    def validate_name(self, value):
        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError(
                "Nazwa może zawierać tylko litery i znaki spacji!",
            )
        return value

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['id', 'title', 'text', 'topic', 'slug', 'created_at', 'updated_at', 'created_by']
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']