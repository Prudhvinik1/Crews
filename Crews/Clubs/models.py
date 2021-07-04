from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_dp = models.ImageField(blank=True,null=True,upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ("User")    
        
        verbose_name_plural = ("Users")

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
    
            return reverse("User_detail", kwargs={"pk": self.pk})

class Club(models.Model):
    club_name = models.CharField(max_length=30)
    club_description = models.CharField(max_length=1500)
    club_startdate = models.TimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    club_logo = models.ImageField(blank=True,null=True,upload_to=None, height_field=None, width_field=None, max_length=None)
    club_tandc = models.FileField(blank=False, upload_to=None)    
    
    class Meta:
        verbose_name = ("Club")
        verbose_name_plural = ("Clubs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse("Club_detail", kwargs={"pk": self.pk})
    