from django.urls import path

from AppPelis import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('pelicula', views.peliculas, name="Peliculas"),
    path('directores', views.directores, name="Directores"),
    path('actores', views.actores, name="Actores"),
    path('buscar/', views.buscar),
    path('busquedaPeli', views.busquedaPeli, name='BusquedaPeli')
   
]
