from django.shortcuts import render, get_object_or_404
from .models import Menu, Reservation, Type
from .forms import ReservationForm
from django.http import HttpResponseRedirect


# Create your views here.
def menu(request):
    types = Type.objects.all()
    return render(request, 'jfood/Menu.html', {'types': types})

def category_menu(request, pk):
    type = get_object_or_404(Type, pk=pk)
    menu_items = Menu.objects.filter(type_name=type)
    return render(request, 'jfood/category_menu.html', {'type': type, 'menu_items': menu_items})

def get_reserv(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            new = Reservation(name=result['name'], phone=result['phone'], date=result['date'])
            new.save()
            return HttpResponseRedirect('/')
    else:
        form = ReservationForm()
    return render(request, 'jfood/Reservation.html', {'form': form})

def about(request):

    return render(request, 'jfood/about.html')
