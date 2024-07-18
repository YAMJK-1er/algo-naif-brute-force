from django.urls import path

from .views import algoNaifBruteForceView

urlpatterns = [
    path('', algoNaifBruteForceView, name="index")
]