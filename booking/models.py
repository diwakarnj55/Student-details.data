from django.db import models

time = (
    ("09","09.00 to 10.30"),
    ("1030","10.30 to 12.00"),
    ("12","12.00 to 01.30"),
    ("02","02.00 to 03.30"),
    ("330","03.30 to 05.00"),
    ("saturday","Saturday"),
    )
status = (
    ("doing","Doing"),
    ("complete","Complete"),
    ("break","Break"),
    ("drop","Drop")
    )
class Course(models.Model):
    course=models.TextField(max_length=5)
    def __str__(self):
        return self.course
class Student(models.Model):
    Invoiceno=models.TextField(max_length=5)
    Name=models.TextField(max_length=40)
    Course_course=models.ForeignKey(Course, models.CASCADE)
    Batchtime=models.CharField(choices=time, max_length=20)
    BSD=models.DateField()
    phone1=models.TextField(max_length=50)
    phone2=models.TextField(max_length=50)
    Place=models.TextField(max_length=50)
    BED=models.DateField(max_length=50)
    Status=models.CharField(choices=status, max_length=50)
    def __str__(self):
        return self.Invoiceno
class Report(models.Model):
    Invoiceno=models.CharField(max_length=5)
    SelectDate=models.DateField(max_length=10)
    Course_SelectSubject=models.ForeignKey(Course, models.CASCADE)
    EnterClassReport=models.TextField(max_length=100)
    def __str__(self):
        return self.Invoiceno
class Fees(models.Model):
    Invoiceno=models.CharField(max_length=5)
    fees=models.CharField(max_length=5)
    duedate=models.DateField(max_length=5)
    def __str__(self):
        return self.Invoiceno
class Exam(models.Model):
    Invoiceno=models.CharField(max_length=5)
    Course_SelectSubject=models.ForeignKey(Course, models.CASCADE)
    date=models.DateField(max_length=5)
    time=models.TimeField(max_length=5)
    def __str__(self):
        return self.Invoiceno



    
