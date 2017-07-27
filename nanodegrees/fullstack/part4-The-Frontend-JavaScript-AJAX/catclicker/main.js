var elements = document.getElementsByClassName("cat");
for(var i=0; i<elements.length; i++) {
  var name = elements[i].innerHTML
  createcat(name);
}

function toggecat(id){

    var elemdiv = document.getElementById(id);
    if(elemdiv.style.display == "none"){
      elemdiv.style.display = "block";
    }
    else{
      elemdiv.style.display = "none"
    }

}

function createcat(s) {
  var thiscat = new Object();
  thiscat.clicks = 0;
  thiscat.name = s;

  //console.log(cats)
  // cconstruct new div
  //var elem = document.getElementById('row-1');
  var elem = $('.catbox');  // jquery
  var div = document.createElement("div");
  div.style.display = "none";
  div.id = s
  var img = document.createElement("img");
  img.src = "img/"+s+".jpg";
  img.alt = s;
  img.height = 159;
  img.width = 240;
  var h3 = document.createElement("h3");
  h3.id = "cat-info"
  h3.innerHTML= s + ", clicks " + thiscat.clicks;

  // add new child
  div.appendChild(img);
  div.appendChild(h3);
  //elem.appendChild(div);
  elem.append(div); // jquery
  img.addEventListener('click', function(){
    thiscat.clicks = thiscat.clicks + 1;
    h3.innerHTML= s + ", clicks " + thiscat.clicks;
  }, false);
}
