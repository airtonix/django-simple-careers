from django.test import TestCase

from models import *

class SimpleTest(TestCase):

    def test_index(self):
        resp = self.client.get('job-index')

    def test_detail(self):
    	simple_requirement, created = Requirement.objects.get_or_create(
    		description="A good sense of humour")

    	job, created = Job.objects.get_or_create(
    		title="Test job", 
    		require=simple_requirement)
    	
    	vacancy, created = Vacancy.objects.get_or_create(
    		job=job)

        resp = self.client.get(vacancy.get_absolute_url())

    def test_application(self):
    	pass