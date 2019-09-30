from django.db import models

class Advertiser(models.Model):
  name   = models.CharField(max_length=100, null = False)
  def __str__(self):
    return self.name

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
  def __str__(self):
    return self.title + '(' + str(self.owner) + ')'
  def incViews(self, ip):
    click = View.objects.create(ip=ip, owner=self)
  def incClicks(self, ip):
    click = Click.objects.create(ip=ip, owner=self)

class Click(models.Model):
  time   = models.DateTimeField(auto_now=True)
  ip     = models.CharField(max_length=15)
  owner  = models.ForeignKey(Ad, null = False, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.owner) + ' at ' + str(self.time)

class View(models.Model):
  time   = models.DateTimeField(auto_now=True)
  ip     = models.CharField(max_length=15)
  owner  = models.ForeignKey(Ad, null = False, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.owner) + ' at ' + str(self.time)
