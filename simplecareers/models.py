import hashlib
import time

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from . import signals


def file_dir(instance, filename):
    
    def timestamp():
        lt = time.localtime(time.time())
        return "%02d%02d%04d%02d%02d%02d" % (lt[2], lt[1], lt[0], lt[3], lt[4], lt[5])

    return "%s%s.%s" % ('careers/resumes/', hashlib.sha1("%s-%s" % ( timestamp(), instance.pk)).hexdigest(), filename.split('.')[-1])



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
    require = models.ForeignKey("Requirement", related_name="openings")
    slug = models.SlugField()
    notify = models.TextField(label = _("comma separated list of email addresses to notify when someone submits an application for this job"))

    def __unicode__(self):
        return self.title


class Vacancy(models.Model):
	""" used to track history of open and closing of positions"""
    opening = models.ForeignKey("Job", related_name="enable_openings")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    expires = models.DateTimeField(blank = True)
    active = models.BooleanField(default = False)

    @models.permalink
    def get_absolute_url(self):
        return ("job-detail", [self.id])

    def __unicode__(self):
        return self.opening.title


class Applicant(models.Model):
    name = models.CharField(max_length=200, unique = True)
    email = models.EmailField(unique  = True )
    phone = models.CharField(max_length=15)
    github = models.URLField(blank=True)
    bitbucket = models.URLField(blank=True)
    dribble = models.URLField(blank=True)
    deviantart = models.URLField(blank=True)
    stackoverflow = models.URLField(blank=True)

    resume = models.FileField(upload_to = file_dir)
    applied_for = models.ForeignKey("Vacancy", related_name="applicants", null = True, blank = True )
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name


post_save.connect(signals.submit_email, sender = Applicant)