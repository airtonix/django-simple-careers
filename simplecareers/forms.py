from django import forms
from django.db import IntegrityError, models
from django.utils.translation import ugettext_lazy as _


Applicant = models.get_model("simplecareers", "Applicant")
Vacancy = models.get_model("simplecareers", "Vacancy")


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label=_("Name"), help_text = _("Enter your full name"))
    email = forms.EmailField(label=_("Email"), help_text = _("Enter your email ie: name@gmail.com"))
    phone = forms.CharField(label=_("Mobile"), help_text = _("Enter your phone"))
    resume = forms.FileField(label=_("Resume"), help_text = _("Attach a file"))
    vacancy = forms.ModelChoiceField(queryset=Vacancy.objects.none(), label=_("Vacancy"), 
        help_text = _("Which vacancy are you submittign this application for?"))
 
    class Meta:
        model = Applicant
        fields = ('name','email','phone','vacancy','resume')

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['vacancy'].queryset = Vacancy.objects.filter()

    def clean_opening(self):
        name = self.cleaned_data.get("opening")
        a = Vacancy.objects.filter(opening__title = name)         
        if not a:
            raise forms.ValidationError("Selecciona una vacante")
        return name

    def get_candidate(self, vacancy=None):

        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        phone = self.cleaned_data["phone"]
        resume = self.cleaned_data["cv"]

        candidate, created = Applicant.objects.get_or_create(name = name, email = email)
        if vacancy:
            candidate.applied_for = vacancy
        candidate.phone = phone
        candidate.save()

        return candidate
   