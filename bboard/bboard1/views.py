from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb, Rubric
from . import forms
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.models import User

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

"""class registre(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register_form.html'
    def form_valid(self, form):
        form.save()
        return super(registre, self).form_valid(form)
    def form_invalid(self, form):
        return super(registre, self).form_invalid(form)"""

def registre(request):
    data = {}
    if request.method == 'POST':
        form = forms.RegistForm(request.POST)
        emal = request.POST.get("email")
        if User.objects.filter(email=emal):
            dat = form
            msg = str("Пользователь с такой электронной почтой уже есть")
            return render(request, 'registration/registr.html', context={'msg': msg, 'form': dat})
        else:
            if form.is_valid():
                form.save()
                dat = form
                msg = str("Регистрация прошла успешно")
                return render(request, 'registration/registr.html', context={'msg': msg, 'form': dat})
            else:
                dat = form
                err = str("Ошибка при регитрации, проверьте совпадают ли пароли")
                return render(request, 'registration/registr.html', context={'msg': err, 'form': dat})
    else:
        form = forms.RegistForm()
        dat = form
        return render(request, 'registration/registr.html', context={'form': dat})