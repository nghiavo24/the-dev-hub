from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostingSerializer
from .models import Posting
# Create your views here.

class PostingView(viewsets.ModelViewSet):
    serializer_class = PostingSerializer
    queryset = Posting.objects.all()
