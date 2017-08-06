var initialCats = [
  {
    clickCount: 0,
    name: "Tabby",
    imgSrc: "img/434164568_fea0ad4013_z.jpg",
    imgAttribution: "https://www.flickr.com/photos/gib",
    nicknames: ["Mr. T"],
  },
  {
    clickCount: 0,
    name: "Tiger",
    imgSrc: "img/22252709_010df3379e_z.jpg",
    imgAttribution: "https://www.flickr.com/photos/gib",
    nicknames: ["Tatab"],
  },
]


var Cat = function(data) {
  this.clickCount = ko.observable(data.clickCount);
  this.name = ko.observable(data.name);
  this.imgSrc = ko.observable(data.imgSrc);
  this.imgAttribution = ko.observable(data.imgAttribution);
  this.nicknames = ko.observableArray(data.nicknames);

  this.title = ko.computed(function() {
    clicks = this.clickCount();
    if(clicks > 20) { return "Adult";}
    if(clicks > 10) { return "Teen";}
    return "Newborn";
  }, this);
}

var ViewModel = function() {
    var self = this;
    this.catList = ko.observableArray([]);

    initialCats.forEach(function(catItem){
      self.catList.push( new Cat(catItem));
    });

    this.currentCat = ko.observable( self.catList()[0] );

    this.incrementCounter = function() {
      this.clickCount( this.clickCount() + 1);
    };

    self.setCat = function(clickedCat) {
       self.currentCat(clickedCat);
    };
}

ko.applyBindings(new ViewModel());
