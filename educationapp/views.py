import csv
from django.shortcuts import render
from .models import courses
from django.http import HttpResponse
from .models import student,StudentAddDetails
# from firebase import firebase as fab
# fa=fab.FirebaseApplication("https://django5-27d69.firebaseio.com/",None)
from .models import faculty
from django.utils.encoding import smart_str

def display(request):
    return render(request,"display.html")


def head(request):
    return render(request,"head.html")


def menu(request):
    return render(request,"menu.html")


def adminlogin(request):
    return render(request,"admin login.html")


def adminlogindetails(request):
    uname=request.POST.get("name")
    upass=request.POST.get("password")
    if uname=="admin" and upass=="admin":
          return render(request,"admin_home.html")
    else:
        return render(request,"admin login.html",{"msg":"invalid user"})


def course(request):
    res=courses.objects.all()
    return render(request,"view course.html",{"msg":res})


def addcourse(request):
    return render(request,"add course.html")


def addcoursedetails(request):
    c_name=request.POST.get("name")
    c_id=request.POST.get("cid")
    c_fee=request.POST.get("cfee")
    c_duration=request.POST.get("cdur")
    c1=courses(coursename=c_name,courseid=c_id,coursefee=c_fee,courseduration=c_duration)
    c1.save()
    return render(request,"add course.html",{"res":"registered your course cuccessfully"})


def coursedelete(request):
    id=request.POST.get("delete_id")
    courses.objects.filter(courseid=id).delete()
    courses.objects.all()
    return course(request)


def courseupdate(request):
    id=request.GET.get("update_id")
    course=courses.objects.filter(courseid=id)
    coursename=''
    courseid=''
    coursefee=''
    courseduration=''
    if course:
        for x in course:
            coursename=x.coursename
            courseid=x.courseid
            coursefee=x.coursefee
            courseduration=x.courseduration
    return render(request,"add course.html",{"cousername":coursename,'courseid':courseid,
                                             'coursefee':coursefee,'courseduration':courseduration})


def coursecsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Course.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"coursename"),
        smart_str(u"courseid"),
        smart_str(u"coursefee"),
        smart_str(u"courseduration"),
    ])
    cl = courses.objects.all()
    for x in cl:
        writer.writerow([
            smart_str(x.coursename),
            smart_str(x.courseid),
            smart_str(x.coursefee),
            smart_str(x.courseduration),
        ])
    return response
    # response=HttpResponse(content_type="text/csv")
    # response['Content-Disposition']='attachment';filename="course.csv"
    # wr=csv.writer(response)
    # cl=courses.objects.all()
    # for x in cl:
    #     wr.writerow([x.coursename,x.courseid,x.coursefee,x.courseduration])
    # return response

def student1(request):
    student=StudentAddDetails.objects.all()
    return render(request,"view_student_details.html",{"student":student})

def viewstudent(request):
    return render(request,"student_register.html")


def studentdetails(request):
    sname=request.POST.get("s1")
    scontact=request.POST.get("s2")
    sgender=request.POST.get("s3")
    susername=request.POST.get("s4")
    spassword=request.POST.get("s5")
    semail=request.POST.get("s6")
    s1=student(name=sname,contect=scontact,gender=sgender,username=susername,password=spassword,email=semail)
    # print(s1)
    s1.save()
    return render(request,"student_register.html",{"res":"registration successfully"})


def studentlogin(request):
    return render(request,"student login.html")


def studentlogindetails(request):
    s_name=request.POST.get("u1")
    s_pass=request.POST.get("u2")
    login=student.objects.filter(username=s_name,password=s_pass)
    if not login:
        return render(request,"student login.html",{"msg2":"invalid details"})
    else:
        return render(request,"student_home.html")


def studentwelcomedetails(request):
    name=request.POST.get("name")
    contact=request.POST.get("contact")
    qualification=request.POST.get("qualification")
    course=request.POST.get("course")
    time=request.POST.get("time")
    StudentAddDetails(name=name,contect=contact,qualification=qualification,course=course,timmeing=time).save()

    # d1={"name":sd1,"qualification":sd3,"course":sd4,"timing":sd5}
    # fa.put("details",sd2,d1)
    return render(request,"student welcome page.html",{"status":"successfuly Added Student Details"})


def studentcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Name"),
        smart_str(u"Contact"),
        smart_str(u"Qualification"),
        smart_str(u"Course"),
        smart_str(u"time"),
    ])
    cl = StudentAddDetails.objects.all()
    for x in cl:
        writer.writerow([
            smart_str(x.name),
            smart_str(x.contect),
            smart_str(x.qualification),
            smart_str(x.course),
            smart_str(x.timmeing)
        ])
    return response

def StudentViewCourse(request):
    res=courses.objects.all()
    return render(request,'student_view_course.html',{"msg":res})    

def StudentViewFaculty(request):
    f=faculty.objects.all()
    return render(request,'student_view_faculty.html',{"fac":f})

def faculty1(request):
    return render(request,"add faculty.html")

def AddStudentDetails(request):
    return render(request,'student welcome page.html')   


def facultydetails(request):
    fct1=request.POST.get("f1")
    fct2=request.POST.get("f2")
    fct3=request.POST.get("f3")
    fct4=request.POST.get("f4")
    fct5=request.POST.get("f5")
    fct6=request.POST.get("f6")
    fct7=request.POST.get("f7")
    fct8=request.POST.get("f8")
    f1=faculty(id=fct1,name=fct2,contact=fct3,gender=fct4,username=fct5,password=fct6,email=fct7,course=fct8)
    f1.save()
    return render(request,"add faculty.html",{"fact":"successfully saved"})


def viewsfaculty(request):
    f=faculty.objects.all()
    return render(request,"view faculty.html",{"fac":f})


def facultydelete(request):
    facd=request.POST.get("del")
    faculty.objects.filter(id=facd).delete()
    faculty.objects.all()
    return viewsfaculty(request)


def facultyupdate(request):
    fid=request.GET.get("fac_update")
    # print(fid)
    faculty.objects.filter(id=fid).update()
    return render(request,"add faculty.html",{"fid":id})

def facultycsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Faculty.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Id"),
        smart_str(u"Name"),
        smart_str(u"Contact"),
        smart_str(u"Gender"),
        smart_str(u"Email"),
        smart_str(u"Course"),
    ])
    cl = faculty.objects.all()
    for x in cl:
        writer.writerow([
            smart_str(x.id),
            smart_str(x.name),
            smart_str(x.contact),
            smart_str(x.gender),
            smart_str(x.email),
            smart_str(x.course)
        ])
    return response