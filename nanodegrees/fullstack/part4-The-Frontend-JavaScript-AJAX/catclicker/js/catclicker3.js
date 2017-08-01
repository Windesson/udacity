$(function() {

    var data = {
        cats: [
	    {
		  img: "img/cat_1.jpg",
      name: "cat_1",
		  id: 0,
		  clicks: 0
		},
		{
		  img: "img/cat_2.jpg",
      name: "cat_2",
		  id: 1,
		  clicks: 0

		},
		{
		  img: "img/cat_3.jpg",
      name: "cat_3",
		  id: 2,
		  clicks: 0
		},
		{
		  img: "img/cat_4.jpg",
      name: "cat_4",
		  id: 3,
		  clicks: 0
		},
		{
		  img: "img/cat_5.jpg",
      name: "cat_5",
		  id: 4,
		  clicks: 0
		},
		]
    };

  var currentcat;

	var octopus = {

		init: function() {
            view.init();
            octopus.displaycat(0);
        },

		getcats: function() {
			return data.cats;
		},

		getcat: function(id) {
            var currentcat = data.cats.filter(function(cat) {
				foundcat = cat.id == id
                return foundcat;
            });
            return currentcat[0];
		},

		displaycat : function(id) {
      currentcat  = octopus.getcat(id)
			cat_view.init(currentcat);
		},

		incrementClicks:  function(id) {
			currentcat.clicks += 1;
		},

    updatecat:  function() {
			currentcat.name = $('#cname').val();
      currentcat.img = $('#cimg').val();

		},


	};


    var view = {
        init: function() {
            this.$catList = $('.cat-clicker');

			// Delegated event to listen for button clicks
            this.$catList.on('click', '.toggleCat', function(e) {
                var id = $(this).attr('id');
				        octopus.displaycat(id);
				return false;
            });

			view.render();
        },
        render: function(){
            var htmlStr = '';
            octopus.getcats().forEach(function(cat){
                htmlStr +=  '<button class="toggleCat" id="' +
				      cat.id + '" >' + cat.name + '</button>';

            });
            this.$catList.html( htmlStr );
        }
    };

    var cat_view = {
        init: function(currentcat) {
     this.$catimg = $('.cat-img');
     this.$catclicks = $('.cat-clicks');
     this.$cname = $('#cname');
     this.$cimg = $('#cimg');
     this.$cupdate = $('#cupdate');

     // Clear and listen
 		  this.$catimg.off('');
      this.$cupdate.off('');

     // Delegated event to listen for button clicks
      this.$catimg.on('click', function(e) {
        octopus.incrementClicks();
        cat_view.render_clicks();
        return false;
      });

      this.$cupdate.on('click', function(e) {
        octopus.updatecat();
        cat_view.render_img();
        cat_view.render_form();
        return false;
      });

		 cat_view.render();
		},

		render: function() {
      cat_view.render_img();
      cat_view.render_clicks();
      cat_view.render_form();
		},

    render_img: function() {
      this.$catimg.attr('src',currentcat.img);
    },

    render_clicks: function() {
      this.$catclicks.html(currentcat.clicks);
    },

    render_form:  function() {
      this.$cimg.val(currentcat.img);
      this.$cname.val(currentcat.name);
    },

    };


	 octopus.init();
}());
