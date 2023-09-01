from django.http import HttpResponse
from django.shortcuts import render
from listings.forms import TaskForm
from listings.models import Task
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'listings/home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'listings/task_list.html',{'tasks':tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
        form = TaskForm()
        return render(request,
                'listings/task_create.html',
                {'form': form})
    else:
        form = TaskForm()

    return render(request,
            'listings/task_create.html',
            {'form': form})

def update_task_status(request, task_id):
    task = Task.objects.get(id=task_id)
    task.finie = not task.finie
    task.save()
    return JsonResponse({'success': True})


