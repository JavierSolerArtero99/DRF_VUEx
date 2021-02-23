from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer
from rest_framework import viewsets


#Admin
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminUser,)


class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.select_related('user')
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            profile = self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist.')

        serializer = self.serializer_class(profile, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileUpdateAPIView(RetrieveAPIView):
    queryset = Profile.objects.select_related('user')
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, username):
        serializer_context = {
            'request': request
        }

        try:
            serializer_instance = self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist.')

        serializer_data = request.data.get('profile', {})
        print(serializer_data)
        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
