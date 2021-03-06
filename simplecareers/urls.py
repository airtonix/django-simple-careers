from django.conf.urls import patterns, url, include
from surlex.dj import surl

from . import views


urlpatterns = patterns("simplecareers.views",
     surl(r"^$", views.JobVacancyListView.as_view(), name="job-index"),
     surl(r"^detail/<id:#>/$", views.JobVacancyDetailView.as_view() , name="job-detail"),
     surl(r"^detail/<id:#>/apply/$", views.JobVacancySubmissionView.as_view(), name="job-application"),
     surl(r"^sent/$", TemplateView.as_view(template_name="simplecareers/sent.html"), name="job-application-sent"),
)