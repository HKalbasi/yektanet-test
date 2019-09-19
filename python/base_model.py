class BaseAdvertising:
    def __init__(self, id = 0):
      self.__clicks = 0
      self.__views = 0
      self.__id = id
    
    def getClicks(self):
      return self.__clicks
    def incClicks(self):
      self.__clicks += 1
    
    def getViews(self):
      return self.__views
    def incViews(self):
      self.__views += 1
    
    def describeMe(self):
      print("I am an instance of the baseAdvertising class\n")