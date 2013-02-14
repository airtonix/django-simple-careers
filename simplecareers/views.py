from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _

from . import models, forms

class JobVacancyListView(ListView):
	model = models.Vacancy
	template_name = 'simplecareers/list.html'

	def get_queryset(self, *args, **kwargs):
		return models.Vacancy.objects.filter(active=True)


class JobVacancyDetailView(DetailView):
	template_name = 'simplecareers/detail.html'
	model = models.Vacancy


class JobVacancySubmissionView(FormView):
	template_name = 'simplecareers/apply.html'
	form_class = forms.ApplicationForm

	def get_success_url(self, *args, **kwrags):
		return reverse_lazy('job-application-sent')

