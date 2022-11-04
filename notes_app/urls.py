from django.urls import path
from . import views

urlpatterns = [
    path('note/', views.NoteListView.as_view(), name ='notes-list-view'), 
    path('note/<int:pk>', views.NoteDetailView.as_view(), name ='notes-details-view'),
]