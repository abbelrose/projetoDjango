from django.urls import path

from . import views  # from recipes import views (. signfica a pasta que estou)

urlpatterns = [
    path('', views.home),
    path('bomdia/', views.bomdia),
    path('recipes/<int:id>/', views.recipe),

]
