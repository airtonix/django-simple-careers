import hashlib

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from . import signals
from . import settings
from . import base


class Requirement(models.Model):
    """ set of requirements """
    description = models.TextField()
    slug = models.SlugField()
    def __unicode__(self):
        return self.description


class Job(models.Model):
    """ The actual available position, describe it here """
    title = models.CharField(max_length=100)
    description = models.TextField()
    require = models.ForeignKey("Requirement", related_name="jobs")
    slug = models.SlugField()
    notify = models.TextField(help_text=_("comma separated list of email addresses to notify when someone submits an application for this job"))

    def __unicode__(self):
        return self.title


class Vacancy(models.Model):
    """ used to track history of open and closing of positions"""
    job = models.ForeignKey("Job")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    expires = models.DateTimeField(null=True, blank = True)
    active = models.BooleanField(default = False)

    @models.permalink
    def get_absolute_url(self):
        return ("job-detail", [self.id])

    def __unicode__(self):
        return self.opening.title



class Applicant(base.ApplicantBaseModel):
    pass

post_save.connect(signals.send_email, sender = Applicant)