from django.urls import path
from .views import insert_words, paragraph_check
urlpatterns = [
    path('', insert_words, name="insert_words"),
    path("check", paragraph_check, name="paragraph_check"),
]
