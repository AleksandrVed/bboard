from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Bb, Rubric
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
def index(request):
#    s = 'Список объявлений\r\n\r\n\r\n'
#    for bb in Bb.objects.order_by('-published'):
#        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    bbs = Bb.objects.all()
    rub = Rubric.objects.all()
    return render(request, "main.html", context={'bbs': bbs, 'rubrics': rub,})

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, "by_rubric.html", context)

class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = forms.BbForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics']=Rubric.objects.all()
        return context