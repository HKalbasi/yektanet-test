from django.db import models

class Advertiser(models.Model):
  name   = models.CharField(max_length=100, null = False)

class Ad(models.Model):
  title  = models.CharField(max_length=100, null = False)
  imgUrl = models.CharField(max_length=1000, null = False)
  link   = models.CharField(max_length=1000, null = False)
  owner  = models.ForeignKey(Advertiser, null = False, on_delete=models.CASCADE)
  approved = models.CharField(
    max_length=2,
    default='PE',
    choices=(
      ('PE','pending'),
      ('RJ','rejected'),
      ('OK','approved'),
    )
  )
  def incClicks(self, ip):
    click = Click.objects.create(ip=ip, owner=self)

class Click(models.Model):
  time   = models.DateTimeField(auto_now=True)
  ip     = models.CharField(max_length=15)
  owner  = models.ForeignKey(Ad, null = False, on_delete=models.CASCADE)

class View(models.Model):
  time   = models.DateTimeField(auto_now=True)
  ip     = models.CharField(max_length=15)
  owner  = models.ForeignKey(Ad, null = False, on_delete=models.CASCADE)
