from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DeleteView

from log import models as log_models


class LogView(View):
    template_name = 'home.html'

    def save_requests(self, request_dict, request_type):
        for key, value in request_dict.items():
            created, log = log_models.Log.objects.get_or_create(
                key=key, value=value, request_type=request_type
            )

    def get(self, request, *args, **kwargs):
        request_dict = request.GET
        request_type = 'GET'

        self.save_requests(request_dict, request_type)

        context = {
            'request_dict': request_dict,
            'request_type': request_type,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        request_dict = request.POST
        request_type = 'POST'

        self.save_requests(request_dict, request_type)

        context = {
            'request_dict': request_dict,
            'request_type': request_type,
        }
        return render(request, self.template_name, context)


class LogListView(ListView):
    model = log_models.Log
    paginate_by = 5


class LogDeleteView(DeleteView):
    model = log_models.Log

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

    def get_success_url(self):
        return reverse('log-list')