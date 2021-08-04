from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

from .models import User
from recipes.models import Subscribe


class UserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'password',)


class UserShowSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField('check_is_subscribed')

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed',)

    def check_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return Subscribe.objects.filter(user=request.user, author=obj).exists()
