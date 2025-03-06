from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
# Create your views here.

def crud_read(request):
    alunos = Aluno.objects.all()
    return render(request, 'crud_read.html', {'alunos': alunos})
def crud_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_read')
    else:
        form = AlunoForm()
    return render(request, 'crud_form.html', {'form':form})
def crud_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('crud_read')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'crud_form.html', {'form': form})
def crud_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('crud_read')
    return render(request, 'confirmacao_delete.html', {'alunos': aluno})