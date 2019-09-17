#include "advertiser.cpp"
#include "ad.cpp"

#define print(x) cout << x << '\n';
#define rep(x) for(int i=0;i<x;i++)

int main(){
  BaseAdvertising baseAdvertising;

  Advertiser advertiser1(1, "name 1");
  Advertiser advertiser2(2, "name 2");

  Ad ad1(1, "img-url1", "link1", &advertiser1);
  Ad ad2(2, "img-url2", "link2", &advertiser2);

  baseAdvertising.describeMe();
  ad2.describeMe();
  advertiser1.describeMe();

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