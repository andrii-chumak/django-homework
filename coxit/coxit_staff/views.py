from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import NewWorkerForm
from .services import workers_dict, hire_worker_service, position_workers_dict



@require_http_methods(["GET"])
def worker_dashboard(request, position=None):
    if position:
        w_dict = position_workers_dict(position)
    else:
        w_dict = workers_dict()

    context = {
        'workers_dict': w_dict,
    }

    return render(request, 'dashboard.html', context)


@require_http_methods(["GET", "POST"])
def hire_worker(request):
    print(request.method)
    if request.method == "POST":
        form = NewWorkerForm(request.POST)
        
        if form.is_valid():
            resp = hire_worker_service(form.cleaned_data)
            return JsonResponse(resp)
        
        return HttpResponse('Your data is incorrect')
        
    form = NewWorkerForm()
    return render(request, 'hire_worker.html', {'form': form, 'success': True}) 