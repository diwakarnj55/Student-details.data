from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="home"),
    path("classreport",views.classreport,name="classreport"),
    path("fees",views.fees,name="fees"),
    path("exam",views.exam,name="exam"),
    path("list",views.list,name="list"),
    path("exam1",views.exam1,name="exam1"),
    path("date",views.date,name="date"),
    path("feeslist",views.feeslist,name="feeslist"),
    path("attendance",views.attendance,name="attendance"),
]