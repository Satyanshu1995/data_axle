from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.IntegerField()
    designation = models.CharField(max_length=50)
    Date_Of_Birth = models.DateField()
    
    def __str__(self):
        return self.name
    
class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()
    
    def __str__(self):
        return self.event_type

class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return self.event_type

class EmailLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    sent_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.status
