from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# Create your views here.


@api_view()
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(["GET"])
def GetNotes(request):
    note =Note.objects.all().order_by('-updated')
    serializer =NoteSerializer(note,many=True)
    return Response (serializer.data)

@api_view(["GET"])
def GetNote(request,pk):
    note =Note.objects.get(id=pk)
    serializer =NoteSerializer(note,many=False)
    return Response (serializer.data)


@api_view(["PUT"])
def UpdateNote(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer= NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def CreateNote(request):
    data =request.data
    note=Note.objects.create(body=data['body'])
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)





@api_view(["DELETE"])
def DeleteNote(request,pk):
    note =Note.objects.get(id=pk)
    note.delete()
    return Response('Note was Deleted !')