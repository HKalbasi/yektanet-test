#include "base_model.cpp"

class Ad : public BaseAdvertising {
  private:
    string title;
    string imgUrl;
    string link;
    Advertiser* owner = NULL;
  public:
    Ad(int _id, string _imgUrl, string _link, Advertiser* _owner) : BaseAdvertising(_id) {
      this->title  = "no-title" ;
      this->imgUrl = _imgUrl;
      this->link   = _link  ;
      this->owner  = _owner ;
    }

    string getLink(){
      return this->link;
    }
    void setLink(string x){
      this->link = x;
    }

    string getImgUrl(){
      return this->imgUrl;
    }
    void setImgUrl(string x){
      this->imgUrl = x;
    }

    void setAdvertiser(Advertiser* x) {
      this->owner = x;
    }

    void describeMe() {
      cout << "I am an Ad\n";
    }

    void incClicks() {
      this->BaseAdvertising::incClicks();
      this->owner->incClicks();
    }
    void incViews() {
      this->BaseAdvertising::incViews();
      this->owner->incViews();
    }
};