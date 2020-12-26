from django.shortcuts import render
from .models import contactUs,Highlights,Faculty,Elite,Infrasturcture,Category,Downloads
# Create your views here.
def home(request):
    if request.method=="POST":
        sname=request.POST['fname']
        semail=request.POST['email']
        smobile=request.POST['contact']
        scourse=request.POST['course']
        contactUs(name=sname,email=semail,mobile=smobile,course=scourse).save()
    hig=Infrasturcture.objects.filter(title='Address')
    dwn=Downloads.objects.all()
    return render(request,'index.html',{'hig':hig,'dwn':dwn})
def abouthistory(request):
    return render(request,'history.html')
def aboutadministration(request):
    infra = Category.objects.all()
    return render(request,'administration.html',{'infra':infra})
def aboutleadership(request):
    return render(request,'leadership.html')
def aboutwhymims(request):
    return render(request,'whymims.html')
def courses(request):
    hig2=Highlights.objects.all()
    return render(request,'courses.html',{'hig2':hig2})
def faculty(request):
    fac=Faculty.objects.all()
    dict={'fac':fac}
    return render(request,'faculty.html',dict)
def elitest(request):
    eli=Elite.objects.all()
    dict={'eli':eli}
    return render(request,'elitest.html',dict)
def description(request,myid):
    print(myid)
    cat=Category.objects.filter(id=myid)
    hig=Infrasturcture.objects.filter(cat=cat[0])
    return render(request,'description.html',{'hig':hig})
def ati(request):
    return render(request,'aboutInstitute.html')