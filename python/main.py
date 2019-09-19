from base_model import *
from ad         import *
from advertiser import *

baseAdvertising = BaseAdvertising()

advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")

ad1 = Ad(1, "img-url1", "link1", advertiser1)
ad2 = Ad(2, "img-url2", "link2", advertiser2)

baseAdvertising.describeMe()
ad2.describeMe()
advertiser1.describeMe()

ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()

ad2.incViews()

ad1.incClicks()
ad1.incClicks()

ad2.incClicks()

print(advertiser2.getName())
advertiser2.setName("new name")
print(advertiser2.getName())
print(ad1.getClicks())
print(advertiser2.getClicks())
print(Advertiser.getTotalClicks())
Advertiser.help()

"""
  rep(4) ad1.incViews();
  ad2.incViews();
  rep(2) ad1.incClicks();
  ad2.incClicks();

  print(advertiser2.getName());
  advertiser2.setName("new name");
  print(advertiser2.getName());
  print(ad1.getClicks());
  print(advertiser2.getClicks());
  print(Advertiser::getTotalClicks());
  Advertiser::help();
}
"""