from django.forms import forms
from django.shortcuts import render

from .models import Feedback


# Create your views here.
def viewbooks(request):
    return render(request, 'usermodule/viewbooks.html')
# views.py

# views.py

from django.shortcuts import render, redirect
from . import froms

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import froms

@login_required
def feedback(request):
    if request.method == 'POST':
        form = Feedback(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Assign the logged-in user to the feedback
            feedback.save()  # Save the feedback to the database
            return redirect('success_url')  # Redirect to a success page
    else:
        form = Feedback()
    return render(request, 'usermodule/feedback.html', {'form': form})



