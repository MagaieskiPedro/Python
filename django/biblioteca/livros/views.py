from django.shortcuts import render,redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
# Create your views here.
def create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = LivroForm()
    return render(request, 'cadastro.html', {'form': form})
def read(request):
    if request.method == 'POST':
        livros = LivroForm(request.POST)
        filtroAutor = livros.data['autor']
        livros = Livro.objects.filter(autor=filtroAutor)
        return render(request, 'consulta.html',{'livros': livros})
    livros = Livro.objects.all()
    return render(request, 'consulta.html',{'livros': livros})
def update(request,pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'cadastro.html', {'form': form})
def delete(request,pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('consulta')
    return render(request, 'deletar.html', {'livro': livro})


