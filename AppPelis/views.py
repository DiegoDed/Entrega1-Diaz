from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppPelis.models import Pelicula, Actor, Director
from AppPelis.forms import PeliculaFormulario

# Create your views here.


def pelicula(request):

      pelicula =  Pelicula(titulo="Titanic", genero="Drama", duracion=203)
      pelicula.save()
      documentoDeTexto = f"--->Pelicula: {pelicula.titulo}   Genero: {pelicula.genero}    Duracion{pelicula.duracion}"

    
      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppPelis/inicio.html")



def actores(request):

      return render(request, "AppPelis/actor.html")



def peliculas(request):

      if request.method == 'POST':

            miFormulario = PeliculaFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:  

                  informacion = miFormulario.cleaned_data

                  pelicula = Pelicula (titulo=informacion['titulo'], genero=informacion['genero'], duracion=informacion['duracion']) 

                  pelicula.save()

                  return render(request, "AppPelis/inicio.html")

      else: 

            miFormulario= PeliculaFormulario() 

      return render(request, "AppPelis/peliculaFormulario.html", {"miFormulario":miFormulario})




def directores(request):

      return render(request, "AppPelis/director.html")






def buscar(request):
      
      if  request.GET["titulo"]:
            titulo = request.GET['titulo'] 
            peliculas = Pelicula.objects.filter(titulo__icontains=titulo)
            return render(request, "AppPelis/inicio.html", {"peliculas":peliculas, "titulo":titulo})

      else: 
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)

def busquedaPeli(request):
      return render(request,'AppPeli/busquedaPeli.html')