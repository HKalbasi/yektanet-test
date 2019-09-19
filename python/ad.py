from base_model import *

class Ad(BaseAdvertising):
  
  def __init__(self, id, imgUrl, link, owner):
    super().__init__(id)
    self.__title  = "no-title"
    self.__imgUrl = imgUrl
    self.__link   = link
    self.__owner  = owner

  def getTitle(self):
    return self.__title
  def setTitle(self, x):
    self.__title = x

  def getImgUrl(self):
    return self.__imgUrl
  def setImgUrl(self, x):
    self.__imgUrl = x

  def getLink(self):
    return self.__link
  def setLink(self, x):
    self.__link = x

  def setAdvertiser(self, x):
    self.__owner = x

  def incClicks(self):
    super().incClicks()
    self.__owner.incClicks()

  def incViews(self):
    super().incViews()
    self.__owner.incViews()