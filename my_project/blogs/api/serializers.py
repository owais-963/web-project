from rest_framework import serializers
from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['tittle', 'post', 'post_date', 'good_name','image']