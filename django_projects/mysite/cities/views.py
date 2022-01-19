from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cities.models import City, State
from cities.forms import StateForm

# Create your views here.


class CityList(LoginRequiredMixin, View):
    def get(self, request):
        sc = State.objects.all().count()
        cl = City.objects.all()

        ctx = {'state_count': sc, 'city_list': cl}
        return render(request, 'cities/city_list.html', ctx)


class StateView(LoginRequiredMixin, View):
    def get(self, request):
        sl = State.objects.all()
        ctx = {'state_list': sl}
        return render(request, 'cities/state_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class StateCreate(LoginRequiredMixin, View):
    template = 'cities/state_form.html'
    success_url = reverse_lazy('cities:all')

    def get(self, request):
        form = StateForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = StateForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class StateUpdate(LoginRequiredMixin, View):
    model = State
    success_url = reverse_lazy('cities:all')
    template = 'cities/state_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = StateForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = StateForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class StateDelete(LoginRequiredMixin, View):
    model = State
    success_url = reverse_lazy('cities:all')
    template = 'cities/state_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = StateForm(instance=make)
        ctx = {'make': make}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class CityCreate(LoginRequiredMixin, CreateView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities:all')


class CityUpdate(LoginRequiredMixin, UpdateView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities:all')


class CityDelete(LoginRequiredMixin, DeleteView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities:all')


# Create your views here.
