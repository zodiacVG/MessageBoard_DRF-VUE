from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class updowmvote(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @action(detail=False,methods=['post'])
    def votedown(self, request, pk=None):
        note = Note.objects.get(commitid=request.data['commitid'])
        note.downvote = note.downvote+1
        note.save()
        return Response()

    @action(detail=False,methods=['post'])
    def voteup(self, request, pk=None):
        note = Note.objects.get(commitid=request.data['commitid'])
        note.upvote = note.upvote+1
        note.save()
        return Response()

   
