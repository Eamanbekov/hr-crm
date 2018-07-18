from django.contrib.auth import get_user_model
from fcm_django.models import FCMDevice
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.notifications.serializers import DeviceSerializer

User = get_user_model()


class CreateDeviceView(CreateAPIView):
    serializer_class = DeviceSerializer
    queryset = FCMDevice.objects.all()

    def create(self, request, *args, **kwargs):
        device = FCMDevice(**request.data)
        device.user = User.objects.get(email='admin@zensoft.io')
        device.save()

        return Response(DeviceSerializer(device).data, status=status.HTTP_201_CREATED)
