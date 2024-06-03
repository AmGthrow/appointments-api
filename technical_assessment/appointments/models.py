from django.db import models


# Create your models here.
class Appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    patients = models.CharField(max_length=30)
    comments = models.TextField()

    def __str__(self):
        time_format = "%I:%M %a %B %d, %Y"
        return f"{self.start_time.strftime(time_format)} - {self.end_time.strftime(time_format)}"
