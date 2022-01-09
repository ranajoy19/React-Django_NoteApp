from . import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes,name="home"),
    path('Notes/',views.GetNotes,name="GetNotes"),
    path('Notes/Create/', views.CreateNote, name="CreateNote"),

    path('Notes/<str:pk>/Update/', views.UpdateNote, name="UpdateNote"),
    path('Notes/<str:pk>/Delete/', views.DeleteNote, name="DeleteNote"),

    path('Notes/<str:pk>/', views.GetNote, name="GetNote")

]
