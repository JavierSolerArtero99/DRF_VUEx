from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False)
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.CharField(allow_blank=True, required=False)
    karma = serializers.IntegerField()
    # image = serializers.SerializerMethodField()
    # following = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'username', 'bio', 'image', 'karma')
        # fields = ('username', 'bio', 'image', 'following',)
        read_only_fields = ('username',)

    # def get_image(self, obj):
    #     if obj.image:
    #         return obj.image

    #     return 'https://static.productionready.io/images/smiley-cyrus.jpg'

    # def get_following(self, instance):
    #     request = self.context.get('request', None)

    #     if request is None:
    #         return False

    #     # if not request.user.is_authenticated():
    #     if not request.user.is_authenticated:
    #         return False

    #     follower = request.user.profile
    #     followee = instance

    #     return follower.is_following(followee)
