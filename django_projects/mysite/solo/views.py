from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.views import View
from django.urls import reverse_lazy

from solo.models import Solo
from solo.forms import BreedForm


class SoloList(LoginRequiredMixin, View):
    template = 'solo/index.html'
    model=Solo

    def get(self, request):
        form= request.session.get('form')
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form= request.POST.get('field1').strip()+" "+request.POST.get('field2').strip()
        request.session['form']=form
        return redirect(request.path)
