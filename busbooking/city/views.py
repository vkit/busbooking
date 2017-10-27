from django.views.generic import ListView, View
from .models import CityDetails
from .forms import CityForm
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages


class CityView(ListView):
    template_name = 'home.html'
    model = CityDetails

    def get_context_data(self, **kwargs):
        context = super(CityView, self).get_context_data(**kwargs)
        context['form'] = CityForm()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        if form.is_valid():
            instance = form.instance
            instance.created_by = self.request.user
            instance.save()
            form.save()
            messages.success(
                request, 'Well done!.')
        else:
            print form.errors
        return HttpResponseRedirect('/city/city_name/')
