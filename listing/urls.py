from django.urls import path
from .views import IndexView,ClientView

urlpatterns = [
    path('', IndexView.as_view()),
    path('create',ClientView.as_view()),
]
