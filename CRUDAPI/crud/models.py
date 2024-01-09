from django.db import models

class Students(models.Model):
    stu_id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email=models.EmailField()
    obtained_marks=models.IntegerField(null=True)
    total_marks=models.IntegerField(null=True)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name