from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View,TemplateView

# Create your views here.

#http methods by using conditional branching (Function based view)
def Fbv(request):
    return HttpResponse('This is Function based view')

#http methods by using seperate Methods(class based view)
class Cbv(View):
    def get(self,request):
        return HttpResponse('This is Class Based View')

#render html page by using FBV
def Fbv_render(request):
    return render(request,'Fbv_render.html')

#render html page by using CBV
class Cbv_render(View):
    def get(self,request):
        return render(request,'Cbv_render.html')
    

#Inserting data by using FBV
def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is Inserted')
    return render(request,'insert_fbv.html',d)

#Inserting data by using CBV
class Insert_Cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Insert_Cbv.html',d)
    
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Is Inserted')

#render html page by using TemplateView
class CBV_Template(TemplateView):
    template_name='CBV_Template.html'




