from django.db import models

# Create your models here.
class Student(models.Model):
    sbd = models.CharField(max_length=8, unique=True)
    foreign_language_code = models.CharField(max_length = 2, null = True, blank= True)

    def __str__(self):
        return self.sbd

class Subject(models.Model):
    code  = models.CharField(max_length = 20, unique = True)
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta: 
        unique_together = ('student', 'subject')
    
    def __str__(self):
        return f"{self.student} - {self.subject}: {self.score}"