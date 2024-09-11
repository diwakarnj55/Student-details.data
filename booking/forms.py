from django import forms
from . models import Report, Fees, Exam
from django.forms import Textarea, TextInput, DateInput, Select, TimeInput

class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        fields =['Invoiceno','SelectDate','Course_SelectSubject','EnterClassReport']
        widgets={
            'Invoiceno':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"invoiceno"
            }),
            'SelectDate':DateInput(attrs={
                "type":"date", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"date"
            }),
            'Course_SelectSubject':Select(attrs={
                "type":"text", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"course"
            }),
            'EnterClassReport':Textarea(attrs={
                "type":"text", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"report"
            }),           
        }
class FeesForm(forms.ModelForm):
    class Meta:
        model=Fees
        fields =['Invoiceno','fees','duedate']
        widgets ={
            'Invoiceno':TextInput(attrs={
                "type":"text ", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"invoiceno"
            }),
            'fees':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"fees",
            }),
            'duedate':DateInput({
                "type":"date", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"duedate",
            }),
        }
class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields =['Invoiceno','Course_SelectSubject','date','time']
        widgets ={
            'Invoiceno':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"invoiceno"
            }),
            'Course_SelectSubject':Select(attrs={
                "type":"text", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"course"      
            }),
            'date':DateInput(attrs={
                "type":"date", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"date",      
            }),
            'time':TimeInput(attrs={
                "type":"time", 
                "class":"form-control", 
                "aria-label":"Sizing example input", 
                "aria-describedby":"inputGroup-sizing-sm",
                "name":"time",         
            }),
        }