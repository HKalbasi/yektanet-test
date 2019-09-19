from base_model import *

class Advertiser(BaseAdvertising):
  __totalClicks = 0
  def __init__(self, id, name):
    super().__init__(id)
    self.__name = name

  def getName(self):
    return self.__name
  def setName(self, x):
    self.__name = x
    
  def incClicks(self):
    super().incClicks()
    self.__class__.__totalClicks += 1
    
  @classmethod
  def getTotalClicks(cls):
    return cls.__totalClicks

  def describeMe(self):
    print("I am an instance of the baseAdvertising class")

  @staticmethod  
  def help():
    print("class e advertiser ye seri method dare")
