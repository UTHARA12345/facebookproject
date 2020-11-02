from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexView(LoginRequiredMixin,ListView):
    model = Fbuser
    template_name = 'fbuser/index.html'

class FbAddView(LoginRequiredMixin, CreateView):
    model = Fbuser
    form_class = FbForm
    template_name = 'fbuser/addfb.html'
    success_url = reverse_lazy('index')

class FbUpdateView(LoginRequiredMixin, UpdateView):
    model = Fbuser
    form_class = FbForm
    template_name = 'fbuser/addfb.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Fbuser, fb_id=id)


class FbDetails(LoginRequiredMixin, DetailView):
    model = Fbuser
    template_name = 'fbuser/fbdetails.html'
    context_object_name = "details"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Fbuser, fb_id=id)

class DeleteFb(LoginRequiredMixin,DeleteView):
    model = Fbuser
    template_name = "fbuser/deletefb.html"
    success_url = reverse_lazy('index')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Fbuser, fb_id=id)


