from rest_framework import serializers 
from .models import Posting, Application, Note

class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ('id','title', 'company', 'posted', 'url', 'note')

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'title', 'company', 'applied', 'hiring_manager', 'compensation', 'work_site', 'location')

class NoteSerializer(serializers.ModelSerializer):
    model = Note
    fields = ('id', 'content')