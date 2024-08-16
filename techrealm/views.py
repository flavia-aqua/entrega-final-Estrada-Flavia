from django.http import HttpResponse
from django.shortcuts import render, redirect
from techrealm.models import *
from techrealm.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

def blogs(request):
    flagBusqueda = False
    if request.method == 'POST':

        tituloBlogs = request.POST.get('titulo')
        blogs = Blogs.objects.filter(titulo__icontains = tituloBlogs)
        flagBusqueda = True
    else:
        blogs = Blogs.objects.all()
    contexto = {"flag": flagBusqueda,"blogs": blogs}
    return render(request, 'blogs.html', contexto)

class blogsDetailView(DetailView):
    model = Blogs
    template_name = "blog_detalle.html"

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid:
            curso = Cursos(nombre = request.POST.get('nombreCurso'), nivel = request.POST.get('nivelCurso'), fecha = request.POST.get('fechaCurso'))
            curso.save()
    return render(request, 'cursos.html')
    
def inicio(request):
    flagBusqueda = False
    if request.method == 'POST':
        nombreCurso = request.POST.get('nombreCurso')
        cursos = Cursos.objects.filter(nombre__icontains = nombreCurso)
        flagBusqueda = True
    else:
        cursos = Cursos.objects.all()
    contexto = {"flag": flagBusqueda,"cursos": cursos}
    return render(request, 'inicio.html', contexto)

def libros(request):
    if request.method == 'POST':
        libro = Libros(nombre = request.POST.get('nombreLibro'), tema = request.POST.get('temaLibro'), codigo = request.POST.get('codigoLibro'))
        libro.save()
    return render(request, 'libros.html')

def login_request(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, "Datos incorrectos")
        else:
            messages.error(request, "Error en el formulario, verifica los datos ingresados")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Usa tu formulario personalizado aquí
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()  # Usa tu formulario personalizado aquí
    
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')

@login_required
def crear_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.autor = request.user.username
            blog.save()
            return redirect('inicio') 
    else:
        form = BlogForm()
    return render(request, 'crear_blog.html', {'form': form})