from django.shortcuts import render,redirect
from . models import Student,Report, Fees,Exam
from . forms import ReportForm, FeesForm, ExamForm
def index(request):
    # data1=""
    # if request.method=='POST':
    #     data2=request.POST['batch']
    #     bt=Student.objects.get(Batchtime=data2)
    #     data1 ={
    #         "bt":bt,
    #     }
    #     return render(request,"index.html",data1)
    if request.method=='POST':
        invoiceno=request.POST['invoiceno']
        form=Student.objects.get(Invoiceno=invoiceno)
        do=Report.objects.get(Invoiceno=invoiceno)
        sum=Fees.objects.get(Invoiceno=invoiceno)
        xam=Exam.objects.get(Invoiceno=invoiceno)
        data ={
            "form":form,
            "do":do,
            "sum":sum,
            "xam":xam,
        }
        return render(request,"index.html",data)
    return render(request,"index.html")
def classreport(request):  
    details=ReportForm()
    data ={
        "details":details,
    }
    if request.method=="POST":
        re=ReportForm(request.POST)
        if re.is_valid():
            re.save()
            return redirect("home")
    return render(request,"classreport.html",data)
def fees(request):
    cash=FeesForm()
    data ={
        "cash":cash,
    }
    if request.method=='POST':
        cash=FeesForm(request.POST)
        if cash.is_valid():
            cash.save()
            return redirect("home")
    return render(request,"fees.html",data)
def exam(request):
    xm=ExamForm()
    data ={
        "xm":xm,
    }
    if request.method=='POST':
        xm=ExamForm(request.POST)
        if xm.is_valid():
            xm.save()
            return redirect("home")
    return render(request,"exam.html",data)
def list(request):
    done=Student.objects.all()
    data ={
        "done":done,
    }
    return render(request,"list.html",data)
def exam1(request):
    if request.method=='POST':
        invoiceno=request.POST['invoiceno']
        form=Student.objects.get(Invoiceno=invoiceno)
        data= {
        "form":form,
        }
        return render(request, "exam1.html",data)
    return render(request, "exam1.html")
def date(request):
    if request.method=='POST':
        date=request.POST['date']
        sum=Fees.objects.get(duedate=date)
        data= {
            "sum":sum,
        }
        return render(request, "date.html",data)
    return render(request, "date.html")    
def feeslist(request):
    amt=Fees.objects.all()
    data ={
        "amt":amt,
    }
    return render(request,"feeslist.html",data)
def attendance(request):
    atten=Student.objects.all()
    if request.method=='POST':
        batch=request.POST['batch']
        form=Student.objects.get(Batchtime=batch)
        data1 ={
            "form":form,
        }
        return render(request,"attendance.html",data1)
    return render(request,"attendance.html",{"atten":atten})