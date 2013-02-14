from django import forms
from django.db import IntegrityError
from django.utils.translation import ugettext_lazy as _

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML
from uni_form.helpers import FormHelper, Submit

from . import models


class ApplicationForm(forms.ModelForm):
    name = form.CharField(label=_("Name"), help_text = _("Enter your full name"))
    email = form.EmailField(label=_("Email"), help_text = _("Enter your email ie: name@gmail.com"))
    phone = form.CharField(label=_("Mobile"), help_text = _("Enter your phone"))
    resume = form.FileField(label=_("Resume"), help_text = _("Attach a file"))
    vacancy = form.ModelChoiceField(queryset=models.Vacancy.objects.none(), label=_("Vacancy"), help_text = _("Which vacancy are you submittign this application for?"))
 
    class Meta:
        model = models.Applicant
        fields = ('name','email','phone','opening','resume')

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['vacancy'].queryset = models.Vacancy.objects.filter()

    def clean_opening(self):
        name = self.cleaned_data.get("opening")
        a = models.Vacancy.objects.filter(opening__title = name)         
        if not a:
            raise form.ValidationError("Selecciona una vacante")
        return name

    def get_candidate(self, vacancy=None):

        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        phone = self.cleaned_data["phone"]
        resume = self.cleaned_data["cv"]

        candidate, created = models.Applicant.objects.get_or_create(name = name, email = email)
        if vacancy:
            candidate.applied_for = vacancy
        candidate.phone = phone
        candidate.save()

        return candidate
   