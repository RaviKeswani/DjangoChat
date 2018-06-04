from django.shortcuts import render,redirect,get_object_or_404
from myapp.forms import StudentFormUpload
from myapp.models import StudentForm
from django.views.generic import *

# Create your views here.
saved=False
def saveStudentForm(request):
    global saved
    if request.method=='GET':
        form=StudentFormUpload()
        return render(request,'stform.html',{'form':form})
    else:
        form=StudentFormUpload(request.POST,request.FILES)
        if form.is_valid():
            s=StudentForm()
            s.first_name=form.cleaned_data['first_name']
            s.last_name = form.cleaned_data['last_name']
            s.father_name = form.cleaned_data['father_name']
            s.dob = form.cleaned_data['dob']
            s.gender = form.cleaned_data[   'gender']
            s.email = form.cleaned_data['email']
            s.city = form.cleaned_data['city']
            s.picture = form.cleaned_data['picture']
            s.save()
            saved=True
        return render(request, 'saved.html', {'saved': saved})


class showInfo(ListView):

    model=StudentForm
    template_name='showinfo.html'

def showStudent(request,student_id):
    model = get_object_or_404(StudentForm,pk=student_id)
    return render(request,'showstudent.html',{'model':model})

# for making API

from rest_framework.generics import ListAPIView
from .models import StudentForm
from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = StudentForm.objects.all()
    serializer_class = PostSerializer
