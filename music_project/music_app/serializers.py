from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model= Song
        feilds= ['id', 'title', 'artist', 'album', 'release_date']