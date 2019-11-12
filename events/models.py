from django.db import models
from accounts.models import group

# Create your models here.

class event(models.Model):
    EID = models.IntegerField(primary_key=True)
    GID = models.ForeignKey(group,on_delete=models.CASCADE)
    Name = models.TextField()
    Description = models.TextField()
    Logo = models.ImageField(upload_to='events/')
    Date = models.DateTimeField()
    Location = models.CharField(max_length=50)
    Registration_Link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.Name
