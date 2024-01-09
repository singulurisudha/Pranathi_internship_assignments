from django.db import models

class Job(models.Model):
    job_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return str(self.job_id)+'  '+self.title

class Candidate(models.Model):
    resume_id=models.AutoField(primary_key=True)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return str(self.resume_id)+' '+str(self.resume)

    