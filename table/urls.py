from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_table, name='statistics_url')
]
