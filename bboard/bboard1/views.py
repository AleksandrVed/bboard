from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Bb, Rubric
from . import forms
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
def index(request):
##    s = 'Список объявлений\r\n\r\n\r\n'
##    for bb in Bb.objects.order_by('-published'):
##        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    bbs = Bb.objects.all()
    rub = Rubric.objects.all()
    paginator = Paginator(bbs, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    return render(request, "bboard1/bb_list.html", context={'obyavleniya': page.object_list, 'rubrics': rub,'page':page})

"""class index(ListView):
    model = Bb
    context_object_name = 'obyavleniya'
    rub = Rubric.objects.all()

    paginator = Paginator(model, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']

    extra_context ={'rubrics': rub}
"""
def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)

    paginator = Paginator(bbs, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)

    context = {'page':page,'bbs': page.object_list, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, "by_rubric.html", context)

class objec(DetailView):
    model = Bb
    template_name = 'detail.html'
    rubrics = Rubric.objects.all()
    extra_context = {'rubrics': rubrics}


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = forms.BbForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics']=Rubric.objects.all()
        return context

class BbUpdateView(UpdateView):
    model = Bb
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('main')

class BbDeleteView(DeleteView):
    model = Bb
    success_url = reverse_lazy('main')