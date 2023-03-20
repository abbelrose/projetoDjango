from django.urls import path

from recipes.views import bomdia, home

urlpatterns = [
    path('', home),
    path('bomdia/', bomdia),

]
