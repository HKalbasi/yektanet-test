from django.db import models

class Advertiser(models.Model):
  name   = models.CharField(max_length=100, null = False)
  clicks = models.IntegerField(default=0)
  views  = models.IntegerField(default=0)

class Ad(models.Model):
  title  = models.CharField(max_length=100, null = False)
  imgUrl = models.CharField(max_length=1000, null = False)
  link   = models.CharField(max_length=1000, null = False)
  owner  = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
  clicks = models.IntegerField(default=0)
  views  = models.IntegerField(default=0)
  def incClicks(self):
    self.clicks += 1
    self.save()