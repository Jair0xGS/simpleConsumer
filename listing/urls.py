from django.urls import path
from .views import IndexView,ClientView,CronogramaView

urlpatterns = [
    path('', IndexView.as_view()),
    path('create',ClientView.as_view()),
    path('cronograma',CronogramaView.as_view()),
]
