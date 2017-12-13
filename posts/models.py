from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=250)
    pub_date=models.DateTimeField(blank=False, default=datetime.now())
    image=models.ImageField(upload_to='media/')
    body=models.TextField()

    def __str__(self):
        return self.title

    #Next function eliminates time from pub_date field
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y %I:%M:%S')

    #This will give summary of post for how many characters you set it to
    def summary(self):
        return self.body[:100]
