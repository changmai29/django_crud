from django.shortcuts import render

from app.models import Notes
from app.serializers import NotesSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.views.generic import ListView
from django.views import View
import json

from rest_framework import filters
from django.db.models import Q
from django.db.models import Count

from django.core.serializers import serialize
from rest_framework.response import Response


class NotesList(View):
    # GET
    def get(self, request):
        id = request.GET.get('id', 0)

        page = request.GET.get('page', 1)
        size = request.GET.get('size', 3)

        limit = int(size)
        offset = (int(page) - 1) * limit

        if id:
            queryset = Notes.objects.filter(id=id)
        else:
            queryset = Notes.objects.all()[offset:offset + limit]
        try:
            notes = []
            serializer_class = NotesSerializer(queryset, many=True)
            for i in range(len(queryset)):
                x = model_to_dict(queryset[i])
                notes.append(x)
            print(notes)
            return JsonResponse({
                "status": "success",
                "code": 200,
                "message": "Data fetched successfully.",
                "page": page,
                "size": size,
                "data": notes
            }, status=200)
        except:
            return JsonResponse({
                "status": "failure",
                "code": 500,
                "message": "Internal server error.",
            }, status=500)

            # POST
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        noteTitle = data['title']
        noteBody = data['body']

        try:
            payload = Notes(
                title=noteTitle,
                body=noteBody,
            )
            payload.save()
            return JsonResponse({
                "status": "success",
                "code": 201,
                "message": "Resources successfully.",
            }, status=200)
        except:
            return JsonResponse({
                "status": "failure",
                "code": 500,
                "message": "Internal server error.",
            }, status=500)

            # PUT

    def put(self, request):
        data = json.loads(request.body)
        id = data['id']
        print(id)
        try:
            note = Notes.objects.get(id=id)
            for key, value in data.items():
                setattr(note, key, value)
            note.save()
            return JsonResponse({
                "status": "success",
                "code": 200,
                "message": "Resources updated successfully.",
            }, status=200)
        except:
            return JsonResponse({
                "status": "error",
                "code": 500,
                "message": "Internal server error.",
            }, status=500)

    # PATCH
    def patch(self, request):
        data = json.loads(request.body)
        id = data['id']
        print(data)
        try:
            note = Notes.objects.get(pk=id)
            for key, value in data.items():
                setattr(note, key, value)
            note.save()
            return JsonResponse({
                "status": "success",
                "code": 200,
                "message": "Resources updated.",
            }, status=200)
        except:
            return JsonResponse({
                "status": "serror",
                "code": 500,
                "message": "RInternal server error.",
            }, status=500)

    # DELETE
    def delete(self, request):
        data = json.loads(request.body)
        id = data['id']
        try:
            note = Notes.objects.filter(id=id)
            if note:
                try:
                    note = Notes.objects.get(pk=id)
                    note.delete()
                    return JsonResponse({
                        "status": "success",
                        "code": 200,
                        "message": "Resource deleted.",
                    }, status=200)
                except:
                    return JsonResponse({
                        "status": "failure",
                        "code": 500,
                        "message": "Internal server error.",
                    }, status=500)
            else:
                return JsonResponse({
                    "status": "error",
                    "code": 404,
                    "message": "Resource dont exist.",
                }, status=404)
        except:
            return JsonResponse({
                "status": "failure",
                "code": 500,
                "message": "Inernal server error.",
            }, status=500)
