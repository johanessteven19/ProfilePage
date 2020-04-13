from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .models import Data

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data_item = form.save(commit=False)
            data_item.save()
            return render(request, 'index.html')
    else:
        form = DataForm()
    return render(request, 'index.html', {'form' : form})

def show(request):
    listname = Data.objects.all()
    context = {'listname': listname}
    return render(request, 'show.html', context)