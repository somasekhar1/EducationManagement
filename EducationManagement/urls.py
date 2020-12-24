"""EducationManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path

from educationapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('display/', views.display),
    path('display/', views.display),
    # path('', views.head),
    path('', views.menu),
    path('admin_login/', views.adminlogin),
    path('admin_login_details/', views.adminlogindetails),
    path('course/', views.course),
    path('addcourse/', views.addcourse),
    path('addcoursedetails/', views.addcoursedetails),
    path('coursedelete/', views.coursedelete),
    path('courseupdate/', views.courseupdate),
    path('coursecsv/', views.coursecsv),

    path('student/', views.student1),
    path('viewstudent/', views.viewstudent),
    path('studentdetails/', views.studentdetails),
    path('studentlogin/', views.studentlogin),
    path('slogin/', views.studentlogindetails),
    path('welcomedetails/', views.studentwelcomedetails),
    path('studentcsv/', views.studentcsv),
    path('student_view_course/',views.StudentViewCourse,name='StudentViewCourse'),
    path('student_view_faculty/',views.StudentViewFaculty,name='StudentViewFaculty'),
    path('add_student/',views.AddStudentDetails,name='AddStudentDetails'),

    path('addfaculty/', views.faculty1),
    path('facultydetails/', views.facultydetails),
    path('faculty/', views.viewsfaculty),
    path('delete/', views.facultydelete),
    path('update/', views.facultyupdate),
    path('facultycsv/',views.facultycsv),

]