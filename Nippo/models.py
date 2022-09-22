from django.db import models

class EmployeeModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
    	return self.name

class DailyReportModel(models.Model):
    topic = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True)
    report = models.TextField()
    comment = models.TextField()
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
    	return self.topic


        

