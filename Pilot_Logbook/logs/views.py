from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Log
from .forms import LogForm

@login_required
def create_log(request):
    if request.method == "POST":
        log_form = LogForm(request.POST)  
        if log_form.is_valid():
            log = log_form.save(commit=False)
            # Link the log to the logged-in user
            log.user = request.user  
            log.save()
            # return render(request,'logs/log_list.html')
            return redirect('logs:logs_list')
    else:
        log_form = LogForm()
    
    return render(request, 'logs/create_log.html', {'log_form': log_form})

@login_required
def log_list(request):
    logs = Log.objects.filter(user=request.user).order_by('-date')  # Show only user's logs
    return render(request, 'logs/log_list.html', {'logs': logs})

@login_required
def edit_log(request, log_id):
    log = get_object_or_404(Log, id=log_id, user=request.user)  # Ensure user can only edit their own logs
    
    if request.method == "POST":
        log_form = LogForm(request.POST, instance=log)
        if log_form.is_valid():
            log_form.save()  # No need to manually assign user again
            return redirect('logs:logs_list')
    else:
        log_form = LogForm(instance=log)

    return render(request, 'logs/edit_log.html', {'log_form': log_form, 'log': log})


@login_required
def delete_log(request, log_id):
    log = get_object_or_404(Log, id=log_id, user=request.user)

    if request.method == "POST":
        log.delete()
        return redirect('logs:logs_list')

    return render(request, 'logs/delete_log.html', {'log': log})
    