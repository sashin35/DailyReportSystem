from django.shortcuts import render,redirect
from .models import *
from .forms import DailyReportForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registerPage(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(request,'nippo/register.html',context)

def loginPage(request):
    form = CreateUserForm(request.POST or None)
    context = {'form':form}
    return render(request,'nippo/login.html',context)

def home(request):
    context= {}
    return render(request,'nippo/dashboard.html',context)

def listPage(request):
    dailyreportList = DailyReportModel.objects.all()
    return render(request,'nippo/list.html',{'list':dailyreportList})

def reportPage(request):
    form = DailyReportForm(request.POST or None)
    if form.is_valid():
        DailyReportModel.objects.create(**form.cleaned_data)
        return redirect('list')
    context = {'form':form}
    return render(request,'nippo/report.html',context)

def updateReport(request,pk):
    report = DailyReportModel.objects.get(id=pk)
    form = DailyReportForm(request.POST or None,instance=report)
    if form.is_valid():
        form.save()
        return redirect('list')
    context = {'form':form}
    return render(request,'nippo/report.html',context)