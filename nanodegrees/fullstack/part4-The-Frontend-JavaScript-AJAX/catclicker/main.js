// list of cat objects
cats = [];

// return cat from the list or false if not found
function getcat(s) {
  for (var i = 0; i < cats.length; i++) {
    if(cats[i].name == s ){
      return cats[i];
    }
  }
  return false;
}

function displaycat(s) {
  // s in the object
  var thiscat = getcat(s);

  // add cat if cat is not in the list
  if(!thiscat){
    var newcat = new Object();
    newcat.clicks = 0;
    newcat.name = s;
    cats.push(newcat)
    thiscat = getcat(s);
  }
  //console.log(cats)

  var elem = document.getElementById('row-1');
  var div = document.createElement("div");
  var img = document.createElement("img");
  img.src = "img/"+s+".jpg";
  img.alt = s;
  img.id = "my-cat";
  img.height = 159;
  img.width = 240;
  var h3 = document.createElement("h3");
  h3.id = "cat-info"
  h3.innerHTML= s + ", clicks " + thiscat.clicks;

  // cleanup last child
  elem.removeChild(elem.firstChild);

  // add new child
  div.appendChild(img);
  div.appendChild(h3);
  elem.appendChild(div);
  img.addEventListener('click', function(){
    thiscat.clicks = thiscat.clicks + 1;
    h3.innerHTML= s + ", clicks " + thiscat.clicks;
  }, false);
}
