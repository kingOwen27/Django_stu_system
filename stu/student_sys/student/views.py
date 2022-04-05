from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import StudentForm
from .models import Student
from django.views import View

class IndexView(View):
    template_name = 'index.html'
    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }
        return context
        
    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)
    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)



