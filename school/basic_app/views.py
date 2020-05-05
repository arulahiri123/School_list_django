from django.shortcuts import render
from basic_app.models import School,Student
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import View,TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView

class Index(TemplateView):
    template_name = 'basic_app/index.html'
class SchoolViewList(ListView):
    model = School
    template_name = 'basic_app/listview.html'

class SchoolDetailView(DetailView):
    context_object_name = 'sch'
    model = School
    template_name = 'basic_app/detailview.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name','location','principal')
    template_name = 'basic_app/createshool.html'

class SchoolUpdate(UpdateView):
    model = School
    fields = ('principal','name')
    template_name = 'basic_app/update.html'

class SchoolDelete(DeleteView):
    model = School
    success_url = reverse_lazy('basic_app:list')
    template_name = 'basic_app/confirm.html'
