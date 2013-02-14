import time
from django.db import models

class ApplicantBaseModel(models.Model):


    def upload_path(self, instance, filename):
        
        def timestamp():
            lt = time.localtime(time.time())
            return "{year}{month}{day}-{hour}{minute}{seconds}".format( 
                year = lt.tm_year, month = lt.tm_month, day = lt.tm_day, 
                hour = lt.tm_hour, minute = lt.tm_min, seconds = lt.tm_sec)

        def filehash():
            return hashlib.sha1( "-".join((timestamp(), instance.pk)) ).hexdigest()

        return os.path.join('careers', 'resumes', filehash()+ filename.split('.')[-1]) 


    name = models.CharField(max_length=200, unique = True)
    email = models.EmailField(unique  = True )
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to=upload_path)

    applied_for = models.ForeignKey("Vacancy", related_name="applicants", null = True, blank = True )
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    finalised = models.BooleanField(default=False)

    class Meta:
        abstract = True


    def __unicode__(self):
        return self.name
