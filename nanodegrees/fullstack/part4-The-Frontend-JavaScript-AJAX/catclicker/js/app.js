$(function() {

    var data = {
        cats: [
	    {
		  name: "cat_1",
		  id: 0,  
		  clicks: 0
		},
		{
		  name: "cat_2",
		  id: 1, 
		  clicks: 0
		  
		},
		{
		  name: "cat_3",
		  id: 2,
		  clicks: 0
		},
		{
		  name: "cat_4",
		  id: 3,
		  clicks: 0
		},
		{
		  name: "cat_5",
		  id: 4,
		  clicks: 0
		},
		]
    };

	
	var octopus = {
		
		init: function() {
            view.init();
        },
		
		getcats: function() {
			return data.cats;
		},
		
		getcat: function(id) {
            var currentcat = data.cats.filter(function(cat) {
				foundcat = cat.id == id
                return foundcat;
            });
			//alert("returning "+JSON.stringify(currentcat))
			
			//return first in the list
            return currentcat[0];
		},
		
		displaycat : function(id) {
			viewpiture.init(id);
		},
		
		upClick:  function(id) {
			cat = octopus.getcat(id);
			cat.clicks += 1; 
            console.log("new num: "+cat.clicks)
		}
		
			
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
	
    var viewpiture = {
        init: function(id) {	
		 this.$catBox = $('.cat-box');
		 this.$catTemplate = $('script[data-template="catbox"]').html();
		 this.currentcat = octopus.getcat(id)
		 
		// Clear and listen
		this.$catBox.off('');
		 
		 // Cache vars 
            var cat = this.currentcat;
		 // Delegated event to listen for button clicks
            this.$catBox.on('click', '.catimg', function(e) {
                var id = $(this).attr('id');
				cat.clicks += 1;
				viewpiture.render();
				return false;
            });
		
		 viewpiture.render();
		},
		
		render: function() {
		    // Cache vars 
            var catBox = this.$catBox,
                catTemplate = this.$catTemplate;				
			
			 // Clear and render
            this.$catBox.html('');
			
			var thisTemplate = catTemplate.replace(/{{id}}/g, this.currentcat.id);
			thisTemplate = thisTemplate.replace(/{{picture}}/g, this.currentcat.name);
			thisTemplate = thisTemplate.replace(/{{clicks}}/g, this.currentcat.clicks);
            catBox.append(thisTemplate);
		},
		
		
    };

	
	 octopus.init();
}());
