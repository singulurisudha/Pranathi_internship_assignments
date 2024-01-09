from django.db import models


class Books(models.Model):
    b_id=models.AutoField(primary_key=True)
    b_name=models.CharField(max_length=120)
    author=models.CharField(max_length=120)

    def __str__(self):
        return str(self.b_name)


class Student(models.Model):
    s_id=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=120)
    book_name=models.ForeignKey(Books,on_delete=models.CASCADE,related_name='books')
    taken=models.BooleanField(default=False)
    returned=models.BooleanField(default=False)

    def __str__(self):
        return self.s_name
    
