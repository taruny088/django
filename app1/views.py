from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def req(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request,'reg.html',{"form":form})
    form=StudentForm()
    return render(request,'reg.html',{"form":form})


def specific_detail(request,id):
    specific=Student.objects.get(id=id)
    return render(request,'specific.html',{'specific':specific})


def details(request):
    data=Student.objects.all()
    return render(request,'details.html',{"data":data})

def update(request,id):
    update_task=Student.objects.get(id=id)
    if request.method == 'POST': 
        form = StudentForm(request.POST, instance=update_task) 
        if form.is_valid(): 
            form.save() 
            return redirect('details')
    else: 
            form = StudentForm(instance=update_task)
    return render(request, 'update.html', {'form': form})

def delete(request,id):
    delete_task=Student.objects.get(id=id)
    delete_task.delete()
    return redirect('details')


    