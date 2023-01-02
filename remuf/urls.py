from django.urls import path

from .views import remufviews

app_name = 'remuf'
urlpatterns = [
    path('list/', remufviews, name='remufList')
]
