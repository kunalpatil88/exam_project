from django.shortcuts import render,redirect
from django.http import HttpResponse
from vehical_managementapp.models import info
# Create your views here.
def infopage(request):
    if request.method=="POST":
        num=request.POST['vehicle_number']
        ty=request.POST['v_type']
        mode=request.POST['model']
        desc=request.POST['Vehicledesc']
        
        p=info.objects.create(num=num, vtype=ty, vmodel=mode, vdesc=desc)
        p.save() 
        return redirect('/dashboard')

    else:

        return render(request,'infopage.html')
def dashboard(request):
    p=info.objects.all()
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)
def edit(request,rid):

  if request.method=="POST":
        unum=request.POST['vehicle_number']
        uty=request.POST['v_type']
        umode=request.POST['model']
        udesc=request.POST['Vehicledesc']
        
        p=info.objects.filter(id=rid)
        p.update(num=unum, vtype=uty, vmodel=umode, vdesc=udesc)
        
        return redirect('/dashboard')
        
    
    
  else:


        p=info.objects.filter(id=rid)
        content={}
        content['data']=p
        return render(request,'editform.html',content)
def delete(request,rid):
    p=info.objects.get(id=rid)
    p.delete()
    return redirect('/dashboard')