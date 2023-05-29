from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django_eventstream import send_event
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


@csrf_exempt
def index(request):
    body = json.loads(request.body)
    send_event(body['channel'], 'message', body['message'])
    return JsonResponse(body)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
