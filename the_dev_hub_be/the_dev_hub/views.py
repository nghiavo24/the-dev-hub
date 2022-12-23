from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostingSerializer, ApplicationSerializer, NoteSerializer
from .models import Posting, Application, Note
# Create your views here.

class PostingView(viewsets.ModelViewSet):
    serializer_class = PostingSerializer
    queryset = Posting.objects.all()

class ApplicationView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()