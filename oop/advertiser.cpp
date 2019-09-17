#ifndef __YEKTANET_ADVERTISER__
#define __YEKTANET_ADVERTISER__

#include "base_model.cpp"

class Advertiser : public BaseAdvertising {
  private:
    string name;
    static int totalClicks;
  public:
    Advertiser(int _id, string _name): BaseAdvertising(_id) {
      this->name = _name;
    }

    string getName(){
      return this->name;
    }
    void setName(string x){
      this->name = x;
    }
    
    void incClicks(){
      this->BaseAdvertising::incClicks();
      Advertiser::totalClicks++;
    }
    static int getTotalClicks() {
      return Advertiser::totalClicks;
    }

    void describeMe() {
      cout << "I am an Advertiser\n";
    }

    static void help() {
      cout << "class e advertiser ye seri method dare\n";
    }
};

int Advertiser::totalClicks;

#endif