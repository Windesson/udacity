
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');
    //var $backgroundImg = $('.bgimg');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");
    //$backgroundImg.remove();

    // load streetview

    // YOUR CODE GOES HERE!
    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var address = streetStr + "," + cityStr;
    var urlStr = "http://maps.googleapis.com/maps/api/streetview?size=600x300&location="+address;


    $greeting.text('So, you want to live at ' + address + '?');

    $body.append('<img class="bgimg" src="'+urlStr+'">');

    var urlNYTimes = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
        urlNYTimes += '?' + $.param({
       'api-key': "b2fd13751f7d4037aaed1045ad33bb2d",
       'sort': "newest",
       'fq': 'glocations:'+'('+address+')',
       'facet_filter': true
    });

   $.getJSON( urlNYTimes , function( data ) {
    console.log(data.response.docs);

    var items = []

    for (i = 0; i < data.response.docs.length; i++) {
        var headline = data.response.docs[i].headline.main;
        var snippet = data.response.docs[i].snippet;
        var url = data.response.docs[i].web_url;
          items.push( "<li class='article'>" +
                         '<a href="'+url+'">'+ headline +"</a>"+
                         '<p>' + snippet +'</p>'+
                         "</li>" );
    }

      $( "<ul/>", {
        "class": "article-list",
        "id": "nytimes-articles",
        html: items.join( "" )
      }).appendTo( $nytElem );
   });

    return false;
};

$('#form-container').submit(loadData);
