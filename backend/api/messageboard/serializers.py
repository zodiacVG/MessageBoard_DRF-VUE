from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=('commitid','content','upvote','downvote','userid','username','committime')
