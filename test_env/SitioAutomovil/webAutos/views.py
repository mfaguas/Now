from django.shortcuts import render
from django.utils import timezone
from .models import Automovil

# Create your views here.
def post_list(request):
    posts = Automovil.objects.filter(Fecha_publicacion__lte=timezone.now()).order_by('Fecha_publicacion')
    return render(request, 'webAutos/post_list.html', {'posts':posts})
