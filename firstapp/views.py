# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration completed successfully!")
            return redirect('register')
        else:
            messages.error(request, "Error in registration. Please check your input.")
    else:
        form = RegistrationForm()

    return render(request, 'form.html', {'form': form})
