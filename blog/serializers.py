from rest_framework import serializers
from .models import *
from core.models import User
import datetime

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ('slug', )