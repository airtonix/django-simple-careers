from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.sites.models import Site

def send_email(sender, **kwargs):
	""" Notify careers manager of a new applicant """

    applicant = kwargs.get("instance")
    send_to = applicant.vacancy.notify
    if not send_to == None and len(send_to) > 0 and isinstance(send_to, str):
    	send_to = send_to.split(",")

    context = {
    	"admin_url" : "http://" + Site.objects.get_current().domain + reverse("admin:index"),
    	"Applicant" : applicant,
    }

    subject = ''.join(render_to_string(
        'simplecareers/mails/admin_notification_subject.html', context).splitlines())
    body = render_to_string('simplecareers/mails/admin_notification_body.html', context)

    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, send_to)
