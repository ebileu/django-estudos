from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno

# Create your views here.
def criar_aluno(request):
    if request.method == "GET":
        status = request.GET.get('status')
        alunos = Aluno.objects.all()
        return render(request, 'criar_aluno.html', {'status': status, 'alunos': alunos})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')

        if len(nome.strip()) == 0:
            return redirect('/aluno/criar_aluno/?status=1')
        if not idade:
            return redirect('/aluno/criar_aluno/?status=2')
        if int(idade) < 0:
            return redirect('/aluno/criar_aluno/?status=3')

        aluno = Aluno(
            nome = nome,
            idade = idade,
            email = email
        )

        aluno.save()

        return redirect('/aluno/criar_aluno/?status=0')


def listar_aluno(request):
    return HttpResponse('Está é a lista de alunos cadastrados no sistema.')

def deletar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('criar_aluno')