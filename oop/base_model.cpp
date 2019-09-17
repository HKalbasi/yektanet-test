#ifndef __YEKTANET_BASE_MODEL__
#define __YEKTANET_BASE_MODEL__

#include <bits/stdc++.h>
using namespace std;

class BaseAdvertising {
  private:
    int id;
    int clicks;
    int views;
  public:
    BaseAdvertising(int _id = 0) {
      this->clicks = 0;
      this->views = 0;
      this->id = _id;
    }
    int getClicks() {
      return this->clicks;
    }
    virtual void incClicks() {
      this->clicks++;
    }
    int getViews() {
      return this->views;
    }
    virtual void incViews() {
      this->views++;
    }
    virtual void describeMe() {
      cout << "I am an instance of the baseAdvertising class\n";
    }
};

#endif