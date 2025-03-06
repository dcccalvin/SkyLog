from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Log
from .forms import LogForm

@login_required
def create_log(request):
    if request.method == "POST":
        log_form = LogForm(request.POST)  
        if log_form.is_valid():
            log = log_form.save(commit=False)
            log.user = request.user  # Link the log to the logged-in user
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
