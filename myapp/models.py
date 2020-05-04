from django.db import models

# Create your models here.

class ActivityRecord(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

class UserData(models.Model):
    real_name = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    activity_periods = models.ManyToManyField(ActivityRecord)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.real_name + '  '+self.time_zone
