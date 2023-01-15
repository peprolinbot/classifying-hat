from django.urls import path

from . import views

app_name = 'classifyingHat'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/<str:results_id>', views.index, name='results'),
    path('api/get_results', views.get_results, name='get_results'),
]
