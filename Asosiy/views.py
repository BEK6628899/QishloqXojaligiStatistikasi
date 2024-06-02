from django.shortcuts import render
from django.views import View
from .models import *


class Home(View):
    def get(self,request):
        data = {'hududbolim':HududiyBolimlar.objects.all(),'ishorni':BoshIsh.objects.all()}
        return render(request,'index.html', data)



class Matbuot(View):
    def get(self,request):
        data = {'matbuotlar':Matbuotlar.objects.all()}
        return render(request,'category.html',data)



class Kontaktlar(View):
    def get(self,request):
        return render(request,'contact.html')



class Yangliklar(View):
    def get(self,request):
        data = {'matbuotlar': Matbuotlar.objects.all()}
        return render(request,'single.html', data)