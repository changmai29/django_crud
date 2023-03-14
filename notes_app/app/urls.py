from django.contrib import admin
from django.urls import path,include
from app.views import NotesViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'notes', NotesViewSet)

urlpatterns = [   
    path('',include(router.urls))   
]